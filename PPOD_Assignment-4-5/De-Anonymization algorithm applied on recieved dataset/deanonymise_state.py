import pandas as pd

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Identify the most frequent 'state' for the entire dataset
most_frequent_state = anonymized_df['state'].mode().iloc[0]

# Replace the anonymized 'state' with the most frequent 'state'
anonymized_df['state'] = most_frequent_state

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_state.csv', index=False)
