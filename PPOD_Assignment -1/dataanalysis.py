import pandas as pd
import numpy as np

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")
titanic_df_pseudonymized = pd.read_csv("titanic_pseudonymized.csv")

# 3.5 Data Analysis
def analyze_information_loss(original_df, transformed_df):
    original_size = original_df.memory_usage().sum()
    transformed_size = transformed_df.memory_usage().sum()
    loss_percentage = ((original_size - transformed_size) / original_size) * 100
    return loss_percentage

# Example usage for data analysis
information_loss_percentage = analyze_information_loss(titanic_df, titanic_df_pseudonymized)
print(f"Information loss percentage: {information_loss_percentage:.2f}%")
