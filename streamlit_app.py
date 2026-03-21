import streamlit as st
import requests

st.title("🚀 Resume JD Matcher")

jd_text = st.text_area("📄 Paste Job Description")
uploaded_files = st.file_uploader("📂 Upload Resumes", type=["pdf"], accept_multiple_files=True)

if st.button("Analyze"):
    if uploaded_files and jd_text:

        url = "https://resume-project-n5ko.onrender.com/match"

        files = []
        for file in uploaded_files:
            files.append(("resumes", (file.name, file, "application/pdf")))

        data = {"jd": jd_text}

        with st.spinner("Analyzing resumes..."):
            response = requests.post(url, files=files, data=data)

            # ✅ DEFINE RESULTS HERE
            results = response.json()

        st.success("Analysis Complete ✅")

        # ✅ NOW LOOP
        for r in results:
            st.subheader(f"📄 {r['name']}")

            st.write(f"🎯 Match Score: {r['score']}%")
            st.write(f"🧠 Semantic Score: {r.get('semantic_score', 'N/A')}%")

            st.write("✅ Matched Skills:", ", ".join(r.get("matched_skills", [])) or "None")
            st.write("❌ Missing Skills:", ", ".join(r.get("missing_skills", [])) or "None")

            # 💡 Suggestions
            suggestions = r.get("suggestions", [])

            if suggestions:
                st.write("💡 Suggestions:")
                for s in suggestions:
                    st.write(f"- {s}")
            else:
                st.write("💡 No suggestions needed 🎉")

            st.markdown("---")