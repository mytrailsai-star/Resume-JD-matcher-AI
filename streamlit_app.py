import requests
import streamlit as st

st.set_page_config(page_title="Resume-JD Matcher", layout="wide")
st.title("📄 Resume-Job Description Matcher")

# Sidebar configuration
st.sidebar.header("Configuration")
api_url = st.sidebar.text_input("API URL", value="http://127.0.0.1:5000")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Resume")
    resume_text = st.text_area("Paste your resume here:", height=300)

with col2:
    st.subheader("Job Description")
    jd_text = st.text_area("Paste the job description here:", height=300)

# Match button
if st.button("🔍 Calculate Match", use_container_width=True):
    if not resume_text or not jd_text:
        st.error("Please provide both resume and job description!")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    f"{api_url}/predict",
                    json={
                        "resume": resume_text,
                        "job_description": jd_text
                    },
                    timeout=10
                )

                if response.status_code == 200:
                    results = response.json()
                    
                    # Display results
                    st.success("✅ Match analysis complete!")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Overall Match %", f"{results['score']:.1f}%")
                    with col2:
                        st.metric("Semantic Match %", f"{results['semantic_score']:.1f}%")
                    with col3:
                        match_count = len(results['matched_skills'])
                        missing_count = len(results['missing_skills'])
                        st.metric("Skills Matched", f"{match_count}/{match_count + missing_count}")
                    
                    # Skills section
                    st.divider()
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ Matched Skills")
                        if results['matched_skills']:
                            for skill in results['matched_skills']:
                                st.write(f"• {skill}")
                        else:
                            st.info("No matched skills found")
                    
                    with col2:
                        st.subheader("❌ Missing Skills")
                        if results['missing_skills']:
                            for skill in results['missing_skills']:
                                st.write(f"• {skill}")
                        else:
                            st.success("All skills matched!")
                
                elif response.status_code == 400:
                    st.error(f"Bad request: {response.json().get('error', 'Unknown error')}")
                else:
                    st.error(f"Backend error (Status {response.status_code}): {response.text}")
            
            except requests.exceptions.ConnectionError:
                st.error(f"❌ Cannot connect to API at {api_url}. Make sure Flask backend is running.")
            except requests.exceptions.Timeout:
                st.error("Request timed out. Backend may be slow.")
            except Exception as e:
                st.error(f"Error: {str(e)}")