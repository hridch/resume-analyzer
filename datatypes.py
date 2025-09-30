from pydantic import BaseModel
from typing import List

class JobMatchScore(BaseModel):
    overall_score: int
    scoring_rationale: str

class MatchingSkills(BaseModel):
    matched: List[str]
    missing: List[str]

class ExperienceMatch(BaseModel):
    summary: str
    years_required: int
    years_present: int

class EducationMatch(BaseModel):
    requirement: str
    candidate: str
    match: bool

class KeywordMatch(BaseModel):
    job_keywords: List[str]
    resume_keywords_found: List[str]
    coverage_percent: int

class Response(BaseModel):
    job_match_score: JobMatchScore
    matching_skills: MatchingSkills
    experience_match: ExperienceMatch
    education_match: EducationMatch
    keyword_match: KeywordMatch
    strengths: List[str]
    gaps: List[str]
    suggested_improvements: List[str]