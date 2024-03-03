import pandas as pd
from cryptography.fernet import Fernet

# Load the original dataset
original_df = pd.read_csv('fatal-police-shootings-data.csv')

# Select columns to be encrypted
columns_to_encrypt = ['name', 'age', 'longitude', 'latitude']

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt selected columns
for column in columns_to_encrypt:
    original_df[column] = original_df[column].apply(lambda x: cipher_suite.encrypt(str(x).encode('utf-8')))

# Save the encrypted dataset
original_df.to_csv('encrypted_fatal_police_shootings_data.csv', index=False)