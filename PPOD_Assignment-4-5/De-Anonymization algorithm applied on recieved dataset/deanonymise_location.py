import pandas as pd

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Function to reverse perturbation for 'longitude' and 'latitude'
def reverse_perturb_location(coord):
    return coord - (0.1 * coord)  # Assuming 10% noise was added during anonymization

# Reverse perturbation for 'longitude' and 'latitude'
anonymized_df['longitude'] = anonymized_df['longitude'].apply(reverse_perturb_location)
anonymized_df['latitude'] = anonymized_df['latitude'].apply(reverse_perturb_location)

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_location.csv', index=False)