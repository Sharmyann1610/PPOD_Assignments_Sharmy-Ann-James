import pandas as pd
import json

# Load the pseudonymous dataset
anonymous_df = pd.read_csv('titanic_anonymized.csv')

# Load the saved generic labels mapping from the JSON file
with open('generic_labels_mapping.json', 'r') as mapping_file:
    generic_labels_mapping = json.load(mapping_file)

# Reverse the keys and values in the mapping for deanonymization
reverse_mapping = {v: k for k, v in generic_labels_mapping.items()}

# Assuming 'country' is the column to deanonymize
# Apply the reverse mapping to the pseudonymous dataset
anonymous_df['country'] = anonymous_df['country'].map(reverse_mapping)

# Save the result as a new CSV file
anonymous_df.to_csv('titanic_country_deanonymized.csv', index=False)