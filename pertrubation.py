import pandas as pd
import numpy as np

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# 3.4 Perturbation
def add_noise(df, attributes_to_perturb):
    for attribute in attributes_to_perturb:
        mean = df[attribute].mean()
        std = df[attribute].std()
        noise = np.random.normal(0, std, df[attribute].shape)
        df[attribute] += noise
    return df

# Example usage for perturbation
attributes_to_perturb = ['age', 'fare']
titanic_df_perturbed = add_noise(titanic_df.copy(), attributes_to_perturb)

# Save result to CSV
titanic_df_perturbed.to_csv("titanic_perturbed.csv", index=False)