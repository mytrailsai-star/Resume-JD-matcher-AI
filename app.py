from flask import Flask, request, jsonify
from matcher import calculate_match, read_pdf, compare_skills
from semantic.semantic_matcher import semantic_similarity

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        resume_text = data.get("resume")
        jd_text = data.get("job_description")
        if not resume_text or not jd_text:
            return jsonify({"error": "Missing 'resume' or 'job_description' field"}), 400

        score = calculate_match(resume_text, jd_text)
        skills = compare_skills(jd_text, resume_text)
        semantic_score = semantic_similarity(resume_text, jd_text)

        matched = skills.get("matched") if isinstance(skills, dict) else []
        missing = skills.get("missing") if isinstance(skills, dict) else []

        return jsonify({
            "score": score,
            "semantic_score": semantic_score,
            "matched_skills": matched,
            "missing_skills": missing
        }), 200

    except Exception as e:
        app.logger.exception("Predict route failed")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")