from flask import Flask, request, jsonify
from matcher import calculate_match, read_pdf, compare_skills

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/match", methods=["POST"])
def match():
    rankings = []
    jd_text = request.form.get("jd")
    files = request.files.getlist("resumes")

    for file in files:
        resume_text = read_pdf(file)

        score = calculate_match(resume_text, jd_text)
        matched, missing = compare_skills(jd_text, resume_text)

        rankings.append({
            "name": file.filename,
            "score": round(score, 2),
            "matched_skills": matched,
            "missing_skills": missing
        })

    rankings.sort(key=lambda x: x["score"], reverse=True)

    return jsonify(rankings)
if __name__ == "__main__":
    app.run(debug=True)
    matched, missing = compare_skills(jd_text, resume_text)