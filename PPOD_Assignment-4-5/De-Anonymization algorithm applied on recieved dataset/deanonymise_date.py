import pandas as pd
from faker import Faker
import random

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Function to reverse pseudonymization for 'date'
def reverse_pseudonymize_date(row):
    return faker.date_between(start_date='-30y', end_date='today')  # Assuming the original dates were within the last 30 years

# Initialize Faker
faker = Faker()

# Reverse pseudonymization for 'date'
anonymized_df['date'] = anonymized_df.apply(reverse_pseudonymize_date, axis=1)

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_date.csv', index=False)