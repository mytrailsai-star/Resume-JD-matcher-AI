from flask import Flask, request, jsonify
from matcher import calculate_match, read_pdf, compare_skills
from semantic.semantic_matcher import semantic_similarity
from matcher import generate_suggestions
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
        skills = compare_skills(jd_text, resume_text)
        
        semantic_score = semantic_similarity(resume_text, jd_text)
        suggestions = generate_suggestions(skills["missing"])
    rankings.append({
          "name": file.filename,
          "score": score,
          "semantic_score": semantic_score,
          "matched_skills": skills["matched"],
          "missing_skills": skills["missing"],
          "suggestions": suggestions   # 👈 NEW
})

    rankings.sort(key=lambda x: x["score"], reverse=True)

    return jsonify(rankings)
if __name__ == "__main__":
    app.run()
    print("JD:", jd_text[:200])
print("Resume:", resume_text[:200])