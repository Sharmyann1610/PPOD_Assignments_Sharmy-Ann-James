import pandas as pd
from faker import Faker

# Load the anonymized dataset without 'name' and 'id'
anonymized_df = pd.read_csv('output_task.csv')  # Replace with the actual path to your anonymized dataset

# Add a new unique 'id' column to the anonymized dataset
anonymized_df['id'] = range(1, len(anonymized_df) + 1)

# Use Faker to generate synthetic names for the 'name' column
faker = Faker()
anonymized_df['name'] = anonymized_df.apply(lambda row: faker.name(), axis=1)

# Save the reestablished dataset with fake 'name' and 'id'
anonymized_df.to_csv('retrieved_name_id.csv', index=False)