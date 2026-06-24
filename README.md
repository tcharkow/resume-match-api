# Resume-Job Match Scorer — API

FastAPI backend for the Resume-Job Match Scorer. Receives a resume and job posting as plain text, returns a match score and skill gap breakdown.

## Endpoint

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/score` | Returns match score, matched skills, and missing skills |

## Request Body

```json
{
  "resume": "plain text resume...",
  "job_posting": "plain text job posting..."
}
```

## Response

```json
{
  "score": 63.8,
  "matched_skills": ["Python", "SQL", "machine learning"],
  "missing_skills": ["NLP", "deep learning", "AWS", "MLOps"],
  "job_skills_found": 21
}
```

## Tech Stack

- Python 3.11
- sentence-transformers 2.7.0
- scikit-learn
- FastAPI
- Uvicorn

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the API: `uvicorn main:app --reload --port 8005`

## Deployment

Deployed on Render. Frontend at nabilmanzo.com/resume-match.