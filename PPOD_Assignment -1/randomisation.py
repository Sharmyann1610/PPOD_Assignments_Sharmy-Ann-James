import pandas as pd
import numpy as np

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# 3.2 Randomisation
def randomize_data(df, attributes_to_randomize):
    for attribute in attributes_to_randomize:
        df[attribute] = df[attribute].apply(lambda x: ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), len(x))))
    return df

# Example usage for randomization
attributes_to_randomize = ['name']
titanic_df_randomized = randomize_data(titanic_df.copy(), attributes_to_randomize)

# Save result to CSV
titanic_df_randomized.to_csv("titanic_randomized.csv", index=False)