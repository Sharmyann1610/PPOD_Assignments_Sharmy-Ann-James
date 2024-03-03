import pandas as pd

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Function to reverse perturbation for 'age'
def reverse_perturb_age(age):
    return age - (0.1 * age)  # Assuming 10% noise was added during anonymization

# Reverse perturbation for 'age'
anonymized_df['age'] = anonymized_df['age'].apply(reverse_perturb_age)

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_age.csv', index=False)
