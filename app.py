from flask import Flask, render_template, request
import os
from resume_parser import extract_text_from_pdf, extract_skills
from model import match_job

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['resume']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        text = extract_text_from_pdf(filepath)
        skills = extract_skills(text)

        job, score = match_job(skills)

        return render_template('result.html',
                               job=job,
                               score=round(score * 100, 2),
                               skills=skills)

if __name__ == '__main__':
    app.run(debug=True)