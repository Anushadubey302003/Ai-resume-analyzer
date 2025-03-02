from flask import Flask, request, jsonify
from etl import extract_resume_text
from model import job_fit_score

app = Flask(__name__)

@app.route('/process_resume', methods=['POST'])
def process_resume():
    data = request.get_json()
    resume_text = data.get("resume_text", "")
    
    # Extract keywords
    extracted_keywords = extract_resume_text(resume_text)
    
    # Compute job-fit score
    score = job_fit_score(extracted_keywords)

    return jsonify({
        "keywords": extracted_keywords,
        "job_fit_score": score
    })

if __name__ == '__main__':
    app.run(debug=True)
