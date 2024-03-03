import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# 3.3 Aggregation
def aggregate_data(df, attributes_to_aggregate):
    for attribute in attributes_to_aggregate:
        df[attribute] = pd.cut(df[attribute], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '21-40', '41-60', '61-80', '81-100'])
    return df

# Example usage for aggregation
attributes_to_aggregate = ['age']
titanic_df_aggregated = aggregate_data(titanic_df.copy(), attributes_to_aggregate)

# Save result to CSV
titanic_df_aggregated.to_csv("titanic_aggregated.csv", index=False)