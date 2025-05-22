from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )

@app.route('/winners', methods=['GET'])
def get_winners():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS winners (id SERIAL PRIMARY KEY, winner TEXT NOT NULL)')
    cur.execute('SELECT id, winner FROM winners')
    winners = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': t[0], 'winner': t[1]} for t in winners])

@app.route('/winners', methods=['POST'])
def create_winner():
    try:
        data = request.json
        print("Datos recibidos:", data)
        
        winner = data.get('winner')
        if not winner:
            return jsonify({'error': 'Missing winner'}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS winners (id SERIAL PRIMARY KEY, winner TEXT NOT NULL)')
        cur.execute('INSERT INTO winners (winner) VALUES (%s)', (winner,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'winner created'}), 201
    except Exception as e:
        print("❌ Error al crear un ganador:", str(e))
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
