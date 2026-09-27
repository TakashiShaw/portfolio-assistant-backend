# Portfolio Assistant Backend

Portfolio Assistant Backend is a rule-based Flask backend for my personal portfolio chatbot. It receives chat messages from my existing portfolio website and returns preset portfolio-related replies based on keyword matching.

The frontend is my existing portfolio website. It sends `POST` requests to the backend's `/chat` route when a visitor asks the chatbot a question.

## Tech Stack

- Flask
- flask-cors
- gunicorn

There are no API keys or private secrets used in this project.

## API Routes

### GET /

Health check route.

Example response:

```json
{"status": "Portfolio Assistant backend is running"}
```

### POST /chat

Receives a user message and returns a chatbot reply.

Request format:

```json
{"message": "What projects have you built?"}
```

Response format:

```json
{"reply": "..."}
```

## Running Locally

Install requirements:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
python app.py
```

The local backend runs on:

```text
http://localhost:5001
```

## Frontend Communication

The portfolio frontend sends a JSON `POST` request to `/chat` with a `message` value. The backend checks the message against keyword categories and returns a JSON object containing a `reply`.

CORS is enabled with `flask-cors` so the portfolio website can communicate with the backend from a different origin.

## Deployment

The backend is deployed on Render. Render provides the `PORT` environment variable used by the Flask app in production.
