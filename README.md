# HW5_.agents
# Resume Keyword Gap Analyzer Skill

## What this skill does
This skill compares a resume with a job description and identifies keyword gaps. It returns matched skills, missing skills, and a match score.

## Why I chose this skill
I chose this task because keyword comparison requires deterministic computation. A script is needed to consistently extract and compare keywords, which cannot be reliably done by a language model alone.

## How to use it
Provide a resume and a job description as input. The skill processes both texts and returns a structured comparison.

To run the script:
```bash
python .agents/skills/resume-keyword-gap-analyzer/scripts/analyze.py

## Test Cases

### 1. Normal Case
Prompt:
Compare my resume with this job description and identify missing skills.

Result:
The skill is triggered, and the script returns matched keywords, missing keywords, and a match score.

---

### 2. Edge Case
Prompt:
Compare this resume: "student" with a job requiring Python, SQL, and machine learning.

Result:
The input is very limited, so the match score is low. This shows the limitation of keyword-based comparison.

---

### 3. Out-of-Scope Case
Prompt:
Rewrite my resume to match this job description.

Result:
The skill should not be triggered because rewriting resumes is outside its scope. The skill is designed only for keyword comparison.

## Video Link
https://youtu.be/HaB9stfjICA
