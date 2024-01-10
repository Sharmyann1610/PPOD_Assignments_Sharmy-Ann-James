import pandas as pd
import networkx as nx
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('titanic.csv')

# Define attributes for generalization
attributes_for_generalization = ['age', 'fare']

# Create a graph for minimal spanning tree
G = nx.Graph()

# Add nodes representing attribute values
for col in attributes_for_generalization:
    attribute_values = sorted(data[col].astype(str).unique())
    G.add_nodes_from(attribute_values)

# Add edges between attribute values with weights based on absolute differences
for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2:
            try:
                val1 = float(node1) if node1 != 'nan' else np.nan  # Convert to numeric if possible
                val2 = float(node2) if node2 != 'nan' else np.nan  # Convert to numeric if possible
                if not np.isnan(val1) and not np.isnan(val2):  # Skip NaN values
                    weight = abs(val1 - val2)  # Calculate weight based on absolute difference
                    G.add_edge(node1, node2, weight=weight)
            except ValueError:
                pass  # Skip if conversion to float fails

# Calculate minimal spanning tree
T = nx.minimum_spanning_tree(G)

# Initialize a dictionary to store mappings of original values to generalized values
generalization_mapping = {}

# Traverse the minimal spanning tree to create a proper mapping for generalization
for edge in T.edges():
    parent_node = min(edge)  # Selecting the minimum node as the parent
    child_node = max(edge)   # Selecting the maximum node as the child

    if child_node not in generalization_mapping:
        generalization_mapping[child_node] = parent_node  # Map child node to parent node

# Apply generalization to the 'age' and 'fare' columns using the mapping
for col in attributes_for_generalization:
    data[col] = data[col].apply(lambda x: generalization_mapping.get(str(x), x))

# Store the anonymized data into a new CSV file
data.to_csv('incognito_titanic.csv', index=False)

# Note: This code demonstrates a simplistic generalization approach based on a minimal spanning tree.
