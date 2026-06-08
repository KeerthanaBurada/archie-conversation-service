# Archie Conversation Layer

The Archie Conversation Layer is responsible for orchestrating communication between the session management service and the AI interview engine.

It retrieves session context, enriches it with problem details, processes canvas snapshots, and produces a standardized AI-ready payload that can be consumed by the interview engine.

---

# Responsibilities

- Retrieve session history from the Session Management Service
- Fetch complete problem context
- Extract and process the latest canvas snapshot
- Build standardized AI payloads
- Forward payloads to the AI Interview Engine
- Provide integration endpoints for testing and debugging

---

# Architecture

```text
Frontend
    ↓
Session Management Service
    ↓
Archie Conversation Layer
    ↓
AI Interview Engine
```

---

# Payload Contract

The conversation layer produces a standardized payload for the AI engine.

```json
{
  "session_id": "...",

  "problem": {
    "id": "...",
    "title": "...",
    "description": "...",
    "requirements": [],
    "constraints": []
  },

  "chat_history": [],

  "canvas_snapshot": {
    "nodes": [],
    "edges": []
  }
}
```

---

# Canvas Handling

The conversation layer consumes persisted canvas data and transforms it into the AI-facing C1 canvas format.

## AI Canvas Snapshot (C1)

```json
{
  "nodes": [
    {
      "id": "n1",
      "type": "service",
      "label": "API Service"
    }
  ],

  "edges": [
    {
      "id": "e1",
      "from": "n1",
      "to": "n2",
      "direction": "one-way"
    }
  ]
}
```

Only the information required for architectural reasoning is included in the AI payload.

Persistence-specific metadata such as node coordinates and editor state are excluded.

---

# Project Structure

```text
app/
│
├── main.py
├── config.py
│
├── routes/
│   └── interview.py
│
├── services/
│   ├── session_service.py
│   ├── problem_service.py
│   ├── payload_builder.py
│   └── ai_service.py
│
├── utils/
│   └── canvas_cleaner.py
│
└── models/
    └── payloads.py
```

---

# Service Components

## session_service.py

Responsible for retrieving session data from the session management service.

Provides:

- Session history retrieval
- Canvas snapshot retrieval
- Session payload extraction

---

## problem_service.py

Responsible for retrieving complete problem information.

Provides:

- Problem metadata
- Requirements
- Constraints
- Interview context

---

## payload_builder.py

Constructs the final AI payload.

Responsibilities:

- Merge session data
- Merge problem context
- Select latest canvas snapshot
- Produce standardized payload

---

## ai_service.py

Responsible for communication with the AI interview engine.

Responsibilities:

- Send payloads to AI endpoint
- Receive AI responses
- Handle downstream integration

---

## interview.py

Exposes API endpoints used for testing and orchestration.

---

# API Endpoints

## Health Check

### GET /

Returns service status.

Response:

```json
{
  "service": "Archie Conversation Service",
  "status": "running"
}
```

---

## Prepare AI Payload

### GET /prepare-ai-payload/{session_id}

Retrieves session data and generates the AI-ready payload.

Response:

```json
{
  "session_id": "...",
  "problem": {...},
  "chat_history": [...],
  "canvas_snapshot": {...}
}
```

---

## Interview Endpoint

### POST /interview/{session_id}

Generates the AI payload and forwards it to the AI interview engine.

Response:

```json
{
  "status": "success",
  "response": {...}
}
```

---

# Configuration

Environment variables:

```env
SESSION_SERVICE_URL=https://sesson-handling.onrender.com

SESSION_SERVICE_API_KEY=YOUR_API_KEY

AI_ENGINE_URL=http://localhost:8001/chat
```

---

# Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the service:

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Current Status

## Completed

- FastAPI service setup
- Session service integration
- Problem service integration
- Payload generation
- Canvas snapshot processing
- Swagger documentation
- Local API testing

## In Progress

- AI endpoint integration
- End-to-end interview flow testing
- Streaming response support
- Production deployment
