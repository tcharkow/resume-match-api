from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once at startup — not on every request
model = SentenceTransformer('all-MiniLM-L6-v2')

SKILLS = [
    "Python", "SQL", "R", "Spark", "Kafka", "Airflow", "Kubernetes",
    "machine learning", "deep learning", "NLP", "TensorFlow", "PyTorch",
    "scikit-learn", "XGBoost", "statistical analysis", "A/B testing",
    "data visualization", "forecasting", "ETL", "dbt", "PostgreSQL",
    "FastAPI", "React", "Power BI", "Excel",
    "AWS", "GCP", "Azure", "MLOps", "model deployment",
    "communication skills", "storytelling with data", "cloud platforms"
]

def extract_skills(text, skill_list):
    text_lower = text.lower()
    found = []
    for skill in skill_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill)
    return found

class ScoreRequest(BaseModel):
    resume: str
    job_posting: str

@app.post("/api/score")
def score_resume(request: ScoreRequest):
    resume_emb = model.encode([request.resume])
    job_emb = model.encode([request.job_posting])
    raw = cosine_similarity(resume_emb, job_emb)[0][0]
    score = round(float(raw) * 100, 1)

    job_skills = extract_skills(request.job_posting, SKILLS)
    resume_skills = extract_skills(request.resume, SKILLS)
    matched = [s for s in job_skills if s in resume_skills]
    missing = [s for s in job_skills if s not in resume_skills]

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "job_skills_found": len(job_skills)
    }