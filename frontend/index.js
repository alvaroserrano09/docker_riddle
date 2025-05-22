const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

const API_URL = process.env.API_URL || 'http://localhost:5000';

app.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${API_URL}/winners`);
        console.log("➡️ Respuesta de la API:", response.data);

        const winners = response.data;
        const list = winners.map(t => `<li>${t.winner}</li>`).join('');
        res.send(`
          <h1>Aula Del Software Libre</h1>
          <h2>Lista de gente pro:</h2>
          <ul>${list}</ul>
        `);
    } catch (err) {
        console.error("❌ Error al conectar con la API:", err.message);
        res.status(500).send('Error al conectar con la API');
    }
});


app.listen(PORT, () => {
    console.log(`Frontend running at http://localhost:${PORT}`);
});
