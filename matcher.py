from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz
import re

# ---------- PDF READER ----------

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

# ---------- TEXT CLEANER ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text

# ---------- MATCH SCORE ---------

def calculate_match(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")

    # Fit only once on JD + resume
    vectors = vectorizer.fit_transform([jd_text, resume_text])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return round(score * 100, 2)

# ---------- SKILL COMPARISON ----------
    def compare_skills(jd_text, resume_text):
          skills_list = [
        "python", "sql", "machine learning", "deep learning",
        "nlp", "flask", "streamlit", "docker", "aws"
    ]

    jd_text = jd_text.lower()
    resume_text = resume_text.lower()

    matched = []
    missing = []

    for skill in skills_list:
        if skill in jd_text:
            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

    return {
        "matched": matched,
        "missing": missing
    }  