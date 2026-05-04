import PyPDF2
import re

SKILLS = ["python", "java", "html", "css", "javascript", "sql", "machine learning"]

SKILL_MAP = {
    "ml": "machine learning",
    "ai": "machine learning",
    "js": "javascript"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def normalize_skills(text):
    words = text.split()
    cleaned = []

    for w in words:
        cleaned.append(SKILL_MAP.get(w, w))

    return " ".join(cleaned)

def extract_text_from_pdf(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""

    text = clean_text(text)          # ✅ FIXED POSITION
    text = normalize_skills(text)

    return text

def extract_skills(text):
    skills_found = []

    for skill in SKILLS:
        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))