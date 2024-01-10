import pandas as pd

# Load the Titanic dataset
titanic_data = pd.read_csv('titanic.csv')

# Define attributes for unique combination discovery and anonymization
attributes_for_combination = ['age', 'class', 'country']

# Function to anonymize based on unique combinations
def anonymize_by_combinations(data):
    # Generate a new identifier column based on unique combinations
    data['Anonymized_ID'] = data[attributes_for_combination].apply(lambda x: '_'.join(x.astype(str)), axis=1)
    
    # Replace original attribute columns with the generated identifier
    data.drop(attributes_for_combination, axis=1, inplace=True)
    
    return data

# Apply the anonymization algorithm
anonymized_titanic = anonymize_by_combinations(titanic_data.copy())

# Store the anonymized data into a new CSV file
anonymized_titanic.to_csv('Combination_discovery_titanic.csv', index=False)
