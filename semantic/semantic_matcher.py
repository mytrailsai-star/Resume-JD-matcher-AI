from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text):
    """
    Basic text cleaning
    """
    return text.lower()


def semantic_similarity(resume_text, jd_text):
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        return round(score * 100, 2)
    except:
        return 0

    # Clean text
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Vectorize
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([text1, text2])

    # Compute similarity
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return round(score * 100, 2)
