import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_resume_text(text):
    """Cleans resume text and extracts key words"""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    doc = nlp(text)
    
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return list(set(keywords))  # Remove duplicates
