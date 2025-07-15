# Dockerized Flask Calculator API

## 📦 Dockerfile Explanation

- *Base Image:* python:3.10-slim – lightweight Python base
- *WORKDIR:* /app – sets working directory inside the container
- *COPY + RUN:* installs dependencies from requirements.txt
- *COPY . .* – copies the rest of the app into container
- *CMD:* runs the Flask app using python app/main.py

---

## 🛠 Build & Run Commands

```bash
docker build -t flask-calculator .
docker run -p 5000:5000 flask-calculator

## curl usage commands

curl.exe -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{\"num1\": 10, \"num2\": 5}'
curl.exe -X POST http://localhost:5000/subtract -H "Content-Type: application/json" -d '{\"num1\": 20, \"num2\": 8}'
curl.exe -X POST http://localhost:5000/multiplication -H "Content-Type: application/json" -d '{\"a\": 6, \"b\": 7}'
curl.exe -X POST http://localhost:5000/div -H "Content-Type: application/json" -d '{\"a\": 100, \"b\": 20}'