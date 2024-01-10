import pandas as pd
import numpy as np

# Load the Titanic dataset from the CSV file
titanic_data = pd.read_csv('titanic.csv')

# Anonymization function using generalization for age and fare columns
def anonymize_dataset(data, k_value):
    # Generalize age into age ranges
    data['age_group'] = pd.cut(data['age'], bins=[0, 18, 30, 50, np.inf], labels=['Child', 'Young Adult', 'Adult', 'Elderly'])

    # Generalize fare into fare classes
    data['fare_class'] = pd.cut(data['fare'], bins=[0, 50, 100, np.inf], labels=['Low', 'Medium', 'High'])

    # Drop original age and fare columns
    data.drop(['age', 'fare'], axis=1, inplace=True)

    # Group by 'age_group' and 'fare_class', calculate count for each combination
    data['count'] = data.groupby(['age_group', 'fare_class']).transform('size')

    # Filter out records where the count is less than k
    anonymized_data = data[data['count'] >= k_value]

    return anonymized_data

# Applying the anonymization function with k = 5 (for example)
k_value = 5
anonymized_titanic = anonymize_dataset(titanic_data, k_value)

# Save anonymized dataset to a CSV file
anonymized_titanic.to_csv('anonymized_titanic.csv', index=False)
