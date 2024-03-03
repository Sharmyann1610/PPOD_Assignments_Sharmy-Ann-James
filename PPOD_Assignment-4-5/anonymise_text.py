import pandas as pd
from faker import Faker
import random

# Load the Titanic dataset
titanic_df = pd.read_csv('titanic.csv')

# Initialize Faker
faker = Faker()

# Define a mapping dictionary for generic labels
generic_labels_mapping = {}

# Function to pseudonymize names using Faker
def pseudonymize_name(name):
    return faker.name()

# Function to anonymize nationalities with a generic label
def anonymize_nationality(nationality):
    if nationality not in generic_labels_mapping:
        generic_labels_mapping[nationality] = f"Nationality_{len(generic_labels_mapping) + 1}"
    return generic_labels_mapping[nationality]

# Function for perturbation by adding noise to numerical data
def perturb_numeric_data(value):
    return str(float(value) + random.uniform(-5, 5))

# Anonymize the data
def anonymize_text(row):
    # Pseudonymize names using Faker
    name = pseudonymize_name(row['name'])

    # Anonymize nationalities
    country = anonymize_nationality(row['country'])

    # Perturb numeric values
    age = perturb_numeric_data(row['age'])
    ticket_number = perturb_numeric_data(row['ticketno'])
    fare = perturb_numeric_data(row['fare'])

    # Replace the original values in the text
    text = f"{name}, a {country} citizen, was a passenger on the Titanic. "
    text += f"He was a {row['gender']}, {age} years of age, traveled on the Titanic with ticket number {ticket_number} and paid a fare of ${fare}. "
    text += f"He {'survived' if row['survived'] == 1 else 'did not survive'} the crash."

    return text

# Open a text file for writing with utf-8 encoding
with open('anonymized_sentences.txt', 'w', encoding='utf-8') as file:
    # Iterate through each row
    for index, row in titanic_df.iterrows():
        # Anonymize the sentence and write it to the file
        anonymized_sentence = anonymize_text(row)
        file.write(anonymized_sentence + '\n\n')
