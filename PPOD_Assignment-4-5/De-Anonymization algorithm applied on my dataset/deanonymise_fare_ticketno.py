import pandas as pd
import random

# Load the anonymized dataset
anonymous_df = pd.read_csv('titanic_deanonymized.csv')

# Assuming 'fare' and 'ticketno' are perturbed numeric columns
# Reverse the perturbation for 'fare'
anonymous_df['fare'] = anonymous_df['fare'] - (0.1 * anonymous_df['fare'].mean() * (2 * random.random() - 1))

# Reverse the perturbation for 'ticketno'
anonymous_df['ticketno'] = anonymous_df['ticketno'] - (0.1 * anonymous_df['ticketno'].mean() * (2 * random.random() - 1))

# Save the reversed dataset
anonymous_df.to_csv('titanic_fare_ticketno_deanonymized.csv', index=False)