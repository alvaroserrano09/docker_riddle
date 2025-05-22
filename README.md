# 🏺 Tadeo Jones y el Misterio del Proyecto Perdido

> Un proyecto olvidado.  
> Un contenedor incompleto.  
> Una aventura para reconstruir una civilización digital...

---

## 📖 Capítulo I – El Despertar

Tadeo Jones, el arqueólogo más despistado del mundo digital, despertó en su escritorio rodeado de tazas vacías, cables USB enredados y líneas de código que no reconocía.

Frente a él, una carpeta: `proyecto-perdido`.  
Dentro, dos subcarpetas misteriosas: `frontend/` y `backend/`.  
En su mente, solo una certeza: **"Esto era importante"**.

---

## 🧩 Capítulo II – Los Fragmentos del Pasado

Tadeo encontró fragmentos de archivos Docker. Vestigios rotos de lo que fue un sistema funcional:

### 🧱 Fragmento Node.js
```Dockerfile
FROM node:latest
WORKDIR /app
COPY package.json .
COPY index.js .
CMD ["node", "index.js"]
```

### 🐍 Fragmento Python
```Dockerfile
FROM python:latest
WORKDIR /app
COPY requirements.txt .
COPY app.py .
CMD ["python", "app.py"]
```

Los fragmentos hablaban de un frontend moderno…  
y un backend en Python, pero faltaba algo…

---

## 🔍 Capítulo III – El Gran Descubrimiento: `docker-compose.yml`

En lo más profundo del proyecto, Tadeo encontró el plano maestro:

```yaml
version: '3.9'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tododb
    volumes:
      - pgdata:/var/lib/postgresql/data

  backend:
    build: ./backend
    depends_on:
      - db
    networks:
      - appnet
    ports:
      - "5000:5000"

  frontend:
    build: ./frontend
    depends_on:
      - backend
    environment:
      API_URL: http://backend:5000
    networks:
      - appnet

volumes:
  pgdata:
```


---

## 📡 Capítulo IV – Cómo levantar el templo

Tadeo sabía que había una sola forma de resucitar el proyecto:

```bash
docker-compose up --build
```

Este comando levantaría los tres servicios:
- Una interfaz web moderna (`frontend`)
- Una API en Python (`backend`)
- Una base de datos PostgreSQL (`db`)

---

## 🧠 Epílogo – Lecciones de un arqueólogo digital

- Usa redes internas (`appnet`) para comunicar contenedores.
- Utiliza variables como `API_URL` para conectar front y back.
- No pongas `localhost` en producción dentro de Docker (¡usa nombres de servicio!).
- Haz copias de seguridad... **siempre.**

---

## 👣 ¿Continuarás tú la aventura?

Si has llegado hasta aquí, la misión es tuya:  
Levanta el proyecto. Investiga. Mejora.  
**Y que el código te acompañe.**

## 🧭 ¿Serás tú quien complete el reto?

Las pistas están sobre la mesa.  
El templo digital está a punto de renacer.  
El misterio aguarda al siguiente valiente desarrollador...
