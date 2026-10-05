from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.analysis.performance_analysis import baseline_evidence
from src.skills.skill_gap import skill_gap
from src.ml.readiness_model import analyze_student


app = FastAPI(
    title="EDU PLUS Member 3 AI/ML API",
    version="1.0.0",
    description="Explainable student readiness and skill-gap analysis API."
)


SUPPORTED_ROLES = {
    "Data Analyst",
    "Backend Developer",
    "Full Stack Developer",
    "Machine Learning Engineer",
    "Embedded Systems Engineer",
}


class StudentReadinessRequest(BaseModel):
    student_id: str
    cgpa: float = Field(ge=0, le=10)
    attendance_percentage: float = Field(ge=0, le=100)
    skills: List[str]
    project_count: int = Field(ge=0)
    certification_count: int = Field(ge=0)
    internship_count: int = Field(ge=0)
    activity_count: int = Field(ge=0)
    career_goal: str


class StudentReadinessResponse(BaseModel):
    student_id: str
    evidence_count: int
    evidence_level: str
    required_skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    priority: str
    recommendations: List[str]


@app.get("/")
def root():
    return {
        "service": "EDU PLUS Member 3 AI/ML API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/v1/student-readiness/ml-profile/{student_id}")
def get_ml_profile(student_id: str):
    """
    Return the machine-learning readiness profile
    for a fictional student from the prototype dataset.
    """

    try:
        return analyze_student(student_id)

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@app.post(
    "/v1/student-readiness/analyze",
    response_model=StudentReadinessResponse
)
def analyze_student_readiness(
    request: StudentReadinessRequest
):
    """
    Analyze a student using:

    1. Explainable rule-based readiness evidence
    2. Skill-gap analysis
    3. Recommendations
    """

    if request.career_goal not in SUPPORTED_ROLES:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported career goal: "
                f"{request.career_goal}. "
                f"Supported roles: {sorted(SUPPORTED_ROLES)}"
            )
        )

    student_data = {
        "cgpa": request.cgpa,
        "attendance_percentage": request.attendance_percentage,
        "project_count": request.project_count,
        "internship_count": request.internship_count,
        "certification_count": request.certification_count,
        "activity_count": request.activity_count,
    }

    # Existing explainable readiness analysis.
    evidence = baseline_evidence(student_data)

    # Existing skill-gap analysis.
    gap = skill_gap(
        request.skills,
        request.career_goal
    )

    return StudentReadinessResponse(
        student_id=request.student_id,
        evidence_count=evidence["evidence_count"],
        evidence_level=evidence["evidence_level"],
        required_skills=gap["required_skills"],
        matched_skills=gap["matched_skills"],
        missing_skills=gap["missing_skills"],
        priority=gap["priority"],
        recommendations=gap["recommendations"],
    )