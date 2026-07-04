# Frontend Integration & C1 Contract Migration
### Demo by Keerthana

---

# Overview

My primary contribution to Archie was integrating the frontend with the backend after major backend changes.

Instead of building new UI screens, I focused on ensuring the frontend and backend communicated correctly using a single C1 Canvas Contract while resolving merge conflicts and rebasing onto the latest main branch.

---

# My Contributions

## 1. C1 Canvas Contract Migration

Migrated the frontend to use the standardized C1 Canvas Contract.

### Canvas Nodes

```json
{
  "id": "n1",
  "type": "service",
  "label": "API Server"
}
```

### Canvas Edges

```json
{
  "from": "n1",
  "to": "n2",
  "direction": "one-way"
}
```

This ensures both frontend and backend follow the exact same schema.

---

## 2. Frontend ↔ Backend Integration

Integrated the React frontend with the FastAPI backend.

Flow:

Candidate

↓

Frontend

↓

POST /chat

↓

FastAPI Backend

↓

Turn Loop

↓

Canvas Parser

↓

Architecture Analyzer

↓

Interview Engine

↓

LLM Provider

↓

AI Response

↓

Frontend

---

## 3. Chat Integration

Updated the frontend chat integration after the backend API changed.

Changes made:

- Updated request payload
- Updated response handling
- Fixed frontend-backend communication
- Verified AI responses display correctly

---

## 4. Rebase & Merge Integration

The feature branch was significantly behind the latest main branch.

Work completed:

- Rebased onto latest main
- Resolved merge conflicts
- Preserved existing backend functionality
- Re-applied only the C1 migration changes
- Fixed integration issues after rebase

---

## 5. Contract Alignment

Resolved multiple contract mismatches between frontend and backend.

Examples:

- from_field → from_
- Updated frontend chat API to match backend response
- Aligned frontend node types with backend C1 contract
- Updated canvas payloads
- Fixed API integration issues

---

# Challenges

## Backend changed during development

The backend evolved while frontend integration was in progress.

Solution:

Rebased the branch and aligned the frontend with the latest backend APIs.

---

## Schema mismatch

Frontend and backend temporarily used different contracts.

Solution:

Migrated everything to the C1 Canvas Contract.

---

## Chat API changes

The backend response format changed.

Solution:

Updated the frontend API client to consume the latest response format.

---

# Impact

- Unified C1 contract across frontend and backend
- Stable frontend-backend communication
- Successful integration after rebase
- Reduced schema inconsistencies
- Successfully merged into the latest main branch

---

# Live Demo

1. Open Archie
2. Select a problem
3. Draw components
4. Connect components
5. Send a message
6. Receive AI response

---

# Key Takeaways

- Frontend and backend now share a common C1 contract.
- The integration layer remains compatible with the latest backend.
- The architecture is easier to maintain because both sides communicate using a single standardized schema.

---

# Thank You
