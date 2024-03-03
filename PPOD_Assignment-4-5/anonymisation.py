import pandas as pd
import hashlib
import random
from faker import Faker
import json

# Load the Titanic dataset
titanic_df = pd.read_csv('titanic.csv')

# Initialize Faker
faker = Faker()

# Define a mapping dictionary for generic labels
generic_labels_mapping = {}

# Function to pseudonymize names using Faker
def pseudonymize_name(_):
    return faker.name()

# Function to anonymize nationalities with a generic label
def anonymize_nationality(nationality):
    if nationality not in generic_labels_mapping:
        generic_labels_mapping[nationality] = f"Nationality_{len(generic_labels_mapping)+1}"
    return generic_labels_mapping[nationality]

# Function for aggregation by grouping sensitive data and applying generalization
def aggregate_and_generalize(df):
    # Group by sensitive columns and apply generalization
    df['age'] = pd.cut(df['age'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '20-40', '40-60', '60-80', '80-100'])
    return df

# Function for perturbation by adding noise to numerical data
def perturb_numeric_data(df, columns):
    for col in columns:
        df[col] = df[col] + (0.1 * df[col].mean() * (2 * random.random() - 1))  # Perturb with 10% noise
    return df

# Function for randomization by shuffling data within a group
def randomize_within_group(df, column, group_column):
    df[column] = df.groupby(group_column)[column].transform(lambda x: x.sample(frac=1).reset_index(drop=True))
    return df

# Apply the masking techniques
# Pseudonymization using Faker for 'name' column
titanic_df['name'] = titanic_df['name'].apply(pseudonymize_name)

# Anonymize nationalities
titanic_df['country'] = titanic_df['country'].apply(anonymize_nationality)

# Save the generic_labels_mapping to a JSON file
with open('generic_labels_mapping.json', 'w') as mapping_file:
    json.dump(generic_labels_mapping, mapping_file)

# Aggregation and generalization
titanic_df = aggregate_and_generalize(titanic_df)

# Perturbation on numeric columns (e.g., Age)
titanic_df = perturb_numeric_data(titanic_df, ['fare','ticketno'])

# Randomization within a group (e.g., within each class)
titanic_df = randomize_within_group(titanic_df, 'ticketno', 'class')

# Save the result as a new CSV file
titanic_df.to_csv('titanic_anonymized.csv', index=False)