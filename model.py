
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

jobs = [
    "python machine learning data science",
    "web development html css javascript",
    "data analyst sql excel python",
    "mobile app development java kotlin"
]

WEIGHTS = {
    "python": 3,
    "machine learning": 4,
    "sql": 2,
    "javascript": 3,
    "excel": 2
}
def weighted_text(skills):
    text = []
    for skill in skills:
        weight = WEIGHTS.get(skill, 1)
        text.extend([skill] * weight)
    return " ".join(text)

def match_job(skills):
    resume_text = weighted_text(skills)

    texts = jobs + [resume_text]

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(texts)

    similarity = cosine_similarity(matrix[-1], matrix[:-1])

    best_index = similarity.argmax()
    score = similarity[0][best_index]

    return jobs[best_index], score