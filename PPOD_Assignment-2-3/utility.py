import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Load original and anonymized Titanic datasets
original_data = pd.read_csv('titanic.csv')
anonymized_data_generalized = pd.read_csv('anonymized_titanic.csv')
anonymized_data_incognito = pd.read_csv('incognito_titanic.csv')
anonymized_data_kmeans = pd.read_csv('k_anonymized_titanic.csv')
anonymized_data_combination = pd.read_csv('custom_titanic.csv')

# Analyzing statistical properties before and after anonymization

# Existing Fields (age, fare) in the original dataset
original_age_fare_stats = original_data[['age', 'fare']].describe()

# New Fields introduced after anonymization (age_group, fare_class, generalized_age, generalized_fare, Anonymized_ID)
anonymized_generalized_age_fare_stats = anonymized_data_generalized[['age_group', 'fare_class']].describe()
anonymized_incognito_age_fare_stats = anonymized_data_incognito[['age', 'fare']].describe()  # If applicable
anonymized_kmeans_age_fare_stats = anonymized_data_kmeans[['generalized_age', 'generalized_fare']].describe()
anonymized_combination_stats = anonymized_data_combination[['Anonymized_ID']].describe()

# Displaying statistics for comparison
print("Original Age and Fare Statistics:")
print(original_age_fare_stats)
print("\nAnonymized Data Statistics - Generalized:")
print(anonymized_generalized_age_fare_stats)
print("\nAnonymized Data Statistics - KMeans:")
print(anonymized_kmeans_age_fare_stats)
print("Anonymized Data Statistics- Incognito:")
print(anonymized_incognito_age_fare_stats)
print("\nAnonymized Data Statistics - Combination Discovery:")
print(anonymized_combination_stats)