import pandas as pd
import matplotlib.pyplot as plt

def analyze_information_loss(original_df, transformed_df):
    original_size = original_df.memory_usage().sum()
    transformed_size = transformed_df.memory_usage().sum()
    loss_percentage = ((original_size - transformed_size) / original_size) * 100
    return loss_percentage

# Load the original dataset
df_original = pd.read_csv('titanic.csv')

# Load the anonymized datasets
df_anonymized1 = pd.read_csv('anonymized_titanic.csv')
df_anonymized2 = pd.read_csv('k_anonymized_titanic.csv')
df_anonymized3 = pd.read_csv('incognito_titanic.csv')
df_anonymized4 = pd.read_csv('Combination_discovery_titanic.csv')

# Calculate the amount of information loss
information_loss1 = analyze_information_loss(df_original, df_anonymized1)
information_loss2 = analyze_information_loss(df_original, df_anonymized2)
information_loss3 = analyze_information_loss(df_original, df_anonymized3)
information_loss4 = analyze_information_loss(df_original, df_anonymized4)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot the degree of information loss for each dataset
axs[0, 0].bar(['Original', 'Anonymized'], [df_original.memory_usage().sum(), df_anonymized1.memory_usage().sum()], color='blue')
axs[0, 0].set_title('Generalisation')
axs[0, 1].bar(['Original', 'Anonymized'], [df_original.memory_usage().sum(), df_anonymized2.memory_usage().sum()], color='red')
axs[0, 1].set_title('k-anonymization')
axs[1, 0].bar(['Original', 'Anonymized'], [df_original.memory_usage().sum(), df_anonymized3.memory_usage().sum()], color='green')
axs[1, 0].set_title('Incognito')
axs[1, 1].bar(['Original', 'Anonymized'], [df_original.memory_usage().sum(), df_anonymized4.memory_usage().sum()], color='orange')
axs[1, 1].set_title('Combination Discovery')

# Set common labels
for ax in axs.flat:
    ax.set(xlabel='Dataset', ylabel='Memory Usage')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

# Display the plot
plt.show()