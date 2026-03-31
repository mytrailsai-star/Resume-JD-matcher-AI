from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text):
    """
    Basic text cleaning
    """
    return text.lower()


def semantic_similarity(resume_text, jd_text):
    """
    Calculate semantic similarity between resume and job description
    """
    try:
        # Clean and vectorize text
        resume_clean = preprocess_text(resume_text)
        jd_clean = preprocess_text(jd_text)
        
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_clean, jd_clean])
        
        # Compute similarity score
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        return round(score * 100, 2)
    except Exception as e:
        print(f"Error in semantic_similarity: {e}")
        return 0
