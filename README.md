# JobPulse

JobPulse is a job search application built with FastAPI, Vue 3, and Elasticsearch.

## Project Structure

- `jobpulse-be/`: FastAPI backend with Elasticsearch integration.
- `jobpulse-fe/`: Vue 3 frontend with Pinia and Tailwind CSS.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Node.js](https://nodejs.org/) (v20 or higher)
- [Python](https://www.python.org/) (v3.10 or higher)

## Local Installation

### 1. Infrastructure (Elasticsearch)

Start the local Elasticsearch instance using Docker Compose:

```bash
docker compose up -d
```

### 2. Backend Setup

Navigate to the backend directory and set up the environment:

```bash
cd jobpulse-be
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

Seed the initial job data into Elasticsearch:

```bash
python seed.py
```

Start the FastAPI development server:

```bash
python main.py
```

The backend will be running at `http://localhost:8000`. You can check the health status at `http://localhost:8000/health`.

### 3. Frontend Setup

Navigate to the frontend directory and install dependencies:

```bash
cd jobpulse-fe
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will be running at `http://localhost:5173`.

## Features

- **Elasticsearch Search**: Real-time job search powered by Elasticsearch.
- **FastAPI Backend**: High-performance API using Python.
- **Vue 3 + Pinia**: Modern frontend state management.
- **Dockerized**: Easy to run local infrastructure.
