import re

STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "for", "on", "with",
    "a", "an", "by", "this", "that", "it", "as", "at"
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    # remove stopwords
    tokens = [word for word in tokens if word not in STOPWORDS]
    return tokens

def extract_keywords(tokens):
    # use unique words as keywords
    return set(tokens)

def analyze(resume_text, jd_text):
    # preprocess both texts
    resume_tokens = preprocess(resume_text)
    jd_tokens = preprocess(jd_text)

    resume_keywords = extract_keywords(resume_tokens)
    jd_keywords = extract_keywords(jd_tokens)

    # compute overlap and gaps
    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    # compute score
    if len(jd_keywords) == 0:
        score = 0
    else:
        score = len(matched) / len(jd_keywords) * 100

    result = {
        "matched_keywords": sorted(list(matched)),
        "missing_keywords": sorted(list(missing)),
        "match_score": round(score, 2)
    }

    return result


# simple test (so you can demo it!)
if __name__ == "__main__":
    resume = """
    Experienced data analyst with skills in Python, SQL, and machine learning.
    """

    job_description = """
    Looking for a candidate with Python, SQL, data analysis, and communication skills.
    """

    result = analyze(resume, job_description)

    print("Matched Keywords:", result["matched_keywords"])
    print("Missing Keywords:", result["missing_keywords"])
    print("Match Score:", result["match_score"], "%")