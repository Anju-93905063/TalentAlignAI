# TalentAlign AI - Resume and JD Text Extractor

TalentAlign AI is a Streamlit-based web application designed to streamline the recruitment process by extracting and comparing raw text from resumes and job descriptions (JD). This helps recruiters and candidates understand how well a resume matches a specific job description using simple text extraction and visualization.

---

## 💡 Features

- 📤 Upload two PDF files: one Resume and one JD.
- 📄 Extract and display raw text using PyMuPDF (`fitz`).
- 🧠 Simple UI for comparing resume and job description content.
- 🧪 Supports real-time preview of uploaded PDF content.
- ⚙️ Easy to run using Streamlit with minimal setup.

---

## 🛠️ Technologies Used

- **Python 3.10**
- **Streamlit**
- **PyMuPDF (fitz)**

---

---

## 🔧 Installation & Setup

### 🔹 1. Clone the repository or download ZIP


-git clone https://github.com/yourusername/talentalign-ai.git
-cd talentalign-ai
Or manually download and unzip the project folder.

🔹 2. Install dependencies
-pip install streamlit PyMuPDF
-

🔹 3. Run the Streamlit app

-streamlit run talentAI.py
-
Or (if streamlit is not in PATH):

-python -m streamlit run talentAI.py
-
The app will open at: http://localhost:8501


---

🖼️ Screenshot

-After running in streamlit
<img width="599" height="293" alt="image" src="https://github.com/user-attachments/assets/af233d1e-3cfd-47b1-8703-6b1d4932b8a6" />



📎 Sample Files
📄 Juspay_SDE_Intern_Job_Description_2025.pdf — Sample Job Description PDF

📄 sample_resume.pdf — Sample Resume PDF for testing the app


<img width="587" height="345" alt="image" src="https://github.com/user-attachments/assets/de16ce9a-08e3-439e-910b-f610195806ed" />


<img width="332" height="369" alt="image" src="https://github.com/user-attachments/assets/362577cd-ad5f-490a-9493-cb813b8bb060" />



-Final
<img width="287" height="347" alt="image" src="https://github.com/user-attachments/assets/820dea58-ba7e-4f3b-a307-f05513f33707" />
