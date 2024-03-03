import pandas as pd

def k_anonymity(dataset, quasi_identifiers, k):
    """
    Perform k-anonymity on the dataset.

    Parameters:
    - dataset: Pandas DataFrame representing the dataset.
    - quasi_identifiers: List of quasi-identifiers to be considered.
    - k: Desired k-anonymity threshold.

    Returns:
    - True if the dataset satisfies k-anonymity, False otherwise.
    """
    # Group records based on quasi-identifiers
    grouped = dataset.groupby(quasi_identifiers)

    # Check if each group has at least k-1 other records
    is_k_anonymous = all(len(group) >= k if len(group) > 1 else True for name, group in grouped)

    return is_k_anonymous

# Load your dataset
your_dataset = pd.read_csv('encrypted_fatal_police_shootings_data.csv')  # Replace with your actual file path and dataset

# Define quasi-identifiers and k value
quasi_identifiers = ['gender', 'age', 'race']  # Adjust based on your dataset
k_threshold = 3  # Adjust based on your desired level of anonymity

# Check if the dataset satisfies k-anonymity
is_k_anonymous = k_anonymity(your_dataset, quasi_identifiers, k_threshold)

# Output the result
if is_k_anonymous:
    print("The dataset satisfies k-anonymity.")
else:
    print("The dataset does not satisfy k-anonymity. Further anonymization is needed.")