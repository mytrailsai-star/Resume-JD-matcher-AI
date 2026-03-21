🚀 Resume – Job Description Matcher AI



An AI-powered full-stack web application that compares resumes with job descriptions and provides:



📊 Match score

🧠 Semantic similarity

🛠️ Skill gap analysis

📈 Ranked resume results

🌐 Live Demohttps: 

Frontend (Streamlit):(https://resume-jd-matcher-ai-2gembszmzre9jnqv75nz8g.streamlit.app/)

Backend API (Render):https://resume-jd-matcher-ai.onrender.com

🧠 Features

📄 Upload multiple resume PDFs

📝 Paste job description

📊 Match scoring using TF-IDF + Cosine Similarity

🧠 Semantic similarity analysis

🛠️ Skill extraction and missing skills detection

📈 Ranked candidate results

🏗️ Architecture

Streamlit (Frontend UI)

&#x20;       ↓

HTTP Request (/match API)

&#x20;       ↓

Flask Backend (Render)

&#x20;       ↓

AI Processing (TF-IDF + Semantic Matching)

&#x20;       ↓

JSON Response

🛠️ Tech Stack

Frontend: Streamlit

Backend: Flask

ML/NLP: Scikit-learn (TF-IDF, Cosine Similarity)

PDF Processing: PyMuPDF

Deployment: Render (Backend), Streamlit Cloud (Frontend)

resume\_jd\_matcher/

│

├── app.py                  # Flask backend

├── matcher.py              # Matching logic

├── streamlit\_app.py        # Streamlit frontend

├── requirements.txt

├── Procfile

│

├── semantic/

│   └── semantic\_matcher.py

│

└── README.md

💡 How It Works

Upload resumes (PDF)

Enter job description

Backend extracts text

TF-IDF vectorization

Cosine similarity computation

Semantic similarity analysis

Skill matching

Returns ranked results

🚀 Future Improvements

BERT-based semantic matching

Resume PDF report generation

Dashboard visualizations

Multi-language support

👩‍💻 Author



Divya Banoth



⭐ Acknowledgements

Streamlit

Flask

Scikit-learn

PyMuPDF

📌 Notes

Local setup uses localhost

Cloud deployment uses public URLs

Backend and frontend must communicate via deployed API URL

README is for documentation only, not execution

