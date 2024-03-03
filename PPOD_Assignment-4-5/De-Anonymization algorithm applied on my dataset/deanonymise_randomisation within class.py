import pandas as pd

# Load the anonymized dataset
anonymous_df = pd.read_csv('titanic_deanonymized.csv')

# Reverse the randomization by sorting the dataset within each 'class' based on the original 'ticketno' order
anonymous_df = anonymous_df.sort_values(by=['class', 'ticketno'])

# Save the reversed dataset
anonymous_df.to_csv('titanic_deanonymise_randomization within class.csv', index=False)