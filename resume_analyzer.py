import spacy
import re
from flask import Flask, request, jsonify

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

# ETL Function: Extract, Transform, Load
def extract_resume_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Clean special characters
    doc = nlp(text)
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return keywords

@app.route('/process_resume', methods=['POST'])
def process_resume():
    data = request.get_json()
    resume_text = data.get("resume_text", "")
    extracted_keywords = extract_resume_text(resume_text)
    return jsonify({"keywords": extracted_keywords})

if __name__ == '__main__':
    app.run(debug=True)
