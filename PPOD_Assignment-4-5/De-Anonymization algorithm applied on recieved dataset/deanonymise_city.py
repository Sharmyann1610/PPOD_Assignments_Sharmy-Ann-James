import pandas as pd

# Load the anonymized dataset
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Identify the most frequent 'city' for each group
mode_city_per_state = anonymized_df.groupby('state')['city'].agg(lambda x: x.mode().iloc[0] if not x.empty else None).to_dict()

# Replace the anonymized 'city' with the mode for each group
anonymized_df['city'] = anonymized_df.apply(lambda row: mode_city_per_state.get(row['state'], None), axis=1)

# Save the deanonymized dataset
anonymized_df.to_csv('deanonymized_output_task_city.csv', index=False)