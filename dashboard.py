import streamlit as st
import requests

st.title("AI-Powered Resume Analyzer")

# Input text area for resume
resume_text = st.text_area("Paste your resume here:", height=200)

if st.button("Analyze Resume"):
    if resume_text:
        # Send request to Flask API
        response = requests.post("http://127.0.0.1:5000/process_resume", json={"resume_text": resume_text})
        
        if response.status_code == 200:
            result = response.json()
            st.subheader("Extracted Keywords:")
            st.write(result["keywords"])
            
            st.subheader("Job Fit Score:")
            st.write(f"{result['job_fit_score']}% match")
        else:
            st.error("Error analyzing resume. Please try again.")
    else:
        st.warning("Please enter resume text.")
