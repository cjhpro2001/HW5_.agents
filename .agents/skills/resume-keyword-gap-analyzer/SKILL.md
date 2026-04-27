---
name: resume-keyword-gap-analyzer
description: Analyze keyword gaps between a resume and a job description by extracting terms, comparing overlaps, and computing a match score. Use this when evaluating resume-job fit.
---

# Resume Keyword Gap Analyzer

## Description
This skill compares a resume with a job description and identifies gaps in keywords. It extracts important terms from both inputs, finds overlaps, and highlights missing skills.

This helps users quickly understand how well their resume matches a specific job.

---

## When to use this skill
Use this skill when:
- You want to compare a resume with a job description
- You need to identify missing or weak skill coverage
- You want a quick, structured keyword match analysis

Do NOT use this skill for:
- rewriting resumes
- generating career advice
- general job search guidance

---

## Inputs
- Resume text (plain text)
- Job description text

---

## Outputs
- Matched keywords
- Missing keywords
- Keyword match score (percentage)
- Structured summary of the comparison

---

## How it works

### Step 1: Preprocess text
The script cleans and normalizes both inputs by:
- converting to lowercase
- removing punctuation
- splitting into tokens

### Step 2: Extract keywords
The script extracts keywords using simple deterministic rules such as filtering out common stopwords.

### Step 3: Compare keywords
- Identify overlapping keywords
- Identify missing keywords from the job description

### Step 4: Compute score
A match score is calculated based on the overlap between the two keyword sets.

---

## Why a script is required

The keyword extraction, comparison, and scoring require deterministic computation.

A language model alone cannot reliably:
- produce consistent keyword sets
- compute exact overlaps
- generate stable match scores

The Python script ensures repeatable and accurate results.

---

## Script
This skill uses:
- scripts/analyze.py

---

## Example usage
User provides:
- Resume text
- Job description

The skill returns:
- A list of matching skills
- A list of missing skills
- A match score