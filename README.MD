# 📄 Resume Analyzer

An interactive app that analyzes your resume against a job description.  
It highlights strengths, gaps, and skill matches while providing scores, keyword coverage, and suggestions to help improve your chances of landing the role.

---

## 🚀 Features
- Upload your resume (PDF)
- Paste or type any job description
- Get:
  - Overall match score
  - Skill matches & missing skills
  - Education alignment
  - Keyword coverage with progress bar
  - Strengths, gaps, and actionable improvements

---

# ⚡ Running the App

There are two recommended ways to run Resume Analyzer:  

---

## ▶️ Running Locally with Python

Clone the repository:
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the Streamlit app:
```bash
streamlit run app.py
```

👉 Open the provided local URL in your browser.

---

## 🐳 Running with Docker Compose

If you prefer containerization (no Python setup required), you can use Docker Compose.  

### Development Mode  
Ideal while actively building: automatically reloads when you edit source files.  
```bash
docker-compose -f docker-compose.dev.yaml up --build
```
👉 Open [http://localhost:8501](http://localhost:8501).

### Production Mode  
Best for deployment: optimized image, runs in the background.  
```bash
docker-compose -f docker-compose.prod.yaml up --build -d
```

Stop production later with:
```bash
docker-compose -f docker-compose.prod.yaml down
```

---

# 📦 Requirements

- **Local setup:** Python 3.8+  
- **Containerized setup:** Docker & Docker Compose  
- See `requirements.txt` for dependencies (used in the local setup)

---

# 💡 Notes
- Ensure any required API keys are configured inside `AIModel`. 
