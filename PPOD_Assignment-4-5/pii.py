import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample sentence
sentence = "John Smith, a Canadian citizen, was a passenger on the Titanic. He was a male, 35 years of age, traveled on the Titanic with ticket number 12345 and paid a fare of $500. He survived the crash."

# Process the sentence with spaCy
doc = nlp(sentence)

# Extract named entities
pii_fields = set()
for ent in doc.ents:
    pii_fields.add(ent.label_)

print("PII Fields to Anonymize:", pii_fields)