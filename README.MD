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

## 🛠️ Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Then open the provided local URL in your browser.

---

## 📦 Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

---

## 💡 Notes 
Make sure you have any required API keys set up inside `AIModel`.
