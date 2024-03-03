import pandas as pd
from faker import Faker

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# 3.1 Pseudonymisation
def pseudonymize_data(df, attributes_to_pseudonymize):
    fake = Faker()
    for attribute in attributes_to_pseudonymize:
        df[attribute] = df[attribute].apply(lambda x: fake.name())
    return df

# Example usage for pseudonymization
attributes_to_pseudonymize = ['name']
titanic_df_pseudonymized = pseudonymize_data(titanic_df.copy(), attributes_to_pseudonymize)

# Save result to CSV
titanic_df_pseudonymized.to_csv("titanic_pseudonymized.csv", index=False)