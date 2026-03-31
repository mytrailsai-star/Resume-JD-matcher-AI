def extract_skills(jd_text, resume_text, skills_list):
    """Extract matched and missing skills"""
    matched = []
    missing = []
    
    for skill in skills_list:
        if skill in jd_text:
            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)
    
    return {
        "matched": matched,
        "missing": missing
    }

def calculate_match(resume_text, jd_text):
    """Calculate overall match score between resume and job description"""
    if not resume_text or not jd_text:
        return 0.0
    
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    
    intersection = len(resume_words & jd_words)
    union = len(resume_words | jd_words)
    
    score = (intersection / union * 100) if union > 0 else 0.0
    return round(score, 2)

def read_pdf(file_path):
    """Read and extract text from PDF file"""
    try:
        import PyPDF2
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def compare_skills(jd_text, resume_text):
    """Compare skills between job description and resume"""
    default_skills = ["Python", "Java", "JavaScript", "SQL", "AWS", "Docker", "Git"]
    return extract_skills(jd_text, resume_text, default_skills)