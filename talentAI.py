import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

st.title("TalentAlign AI - Resume and JD Extractor")
st.markdown("Upload **Resume** and **Job Description (JD)** as PDF files")

uploaded_files = st.file_uploader("Select exactly 2 PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files and len(uploaded_files) == 2:
    resume_file, jd_file = uploaded_files

    st.subheader("📄 Resume - Extracted Text")
    resume_text = extract_text_from_pdf(resume_file)
    st.text_area("Resume Text", resume_text, height=300)

    st.subheader("🧾 Job Description - Extracted Text")
    jd_text = extract_text_from_pdf(jd_file)
    st.text_area("JD Text", jd_text, height=300)

elif uploaded_files and len(uploaded_files) != 2:
    st.warning("⚠️ Please upload exactly 2 PDF files: one Resume and one JD.")
