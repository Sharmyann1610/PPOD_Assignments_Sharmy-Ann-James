import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

# Load the Titanic dataset
data = pd.read_csv('titanic.csv')

# Define attributes for clustering
attributes_for_clustering = ['age', 'fare']

# Prepare data for clustering
X = data[attributes_for_clustering]

# Impute missing values with the mean of each column
imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Determine the value of k for k-anonymity
k_value = 5  # Set the desired k value

# Apply KMeans clustering
kmeans = KMeans(n_clusters=k_value)
data['cluster'] = kmeans.fit_predict(X_imputed)

# Get the centroids of clusters
centroids = pd.DataFrame(kmeans.cluster_centers_, columns=attributes_for_clustering)

# Define function to generalize 'age' and 'fare' based on cluster centroids
def generalize_age_fare(row):
    for col in centroids.columns:
        cluster_value = centroids[col][int(row['cluster'])]
        if row[col] <= cluster_value:
            return f'<={cluster_value:.2f}'
        else:
            return f'>{cluster_value:.2f}'

# Apply generalization to create new columns for generalized 'age' and 'fare'
data['generalized_age'] = data.apply(lambda row: generalize_age_fare(row), axis=1)
data['generalized_fare'] = data.apply(lambda row: generalize_age_fare(row), axis=1)

# Remove original attributes used for clustering and cluster column
data.drop(attributes_for_clustering + ['cluster'], axis=1, inplace=True)

# Store the anonymized data into a new CSV file
data.to_csv('k_anonymized_titanic.csv', index=False)
