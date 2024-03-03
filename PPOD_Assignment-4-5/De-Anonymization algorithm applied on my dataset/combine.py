import pandas as pd

# Read the first CSV file
file1_path = 'titanic_anonymized.csv'
columns_file1 = ['gender', 'embarked', 'sibsp', 'parch', 'survived']
df1 = pd.read_csv(file1_path)

# Read the second CSV file
file2_path = 'titanic_age_deanonymized.csv'
columns_file2 = ['age']
df2 = pd.read_csv(file2_path)

# Read the third CSV file
file3_path = 'titanic_country_deanonymized.csv'
columns_file3 = ['country']
df3 = pd.read_csv(file3_path)

# Read the fourth CSV file
file4_path = 'titanic_fare_ticketno_deanonymized.csv'
columns_file4 = ['fare', 'ticketno']
df4 = pd.read_csv(file4_path)

# Read the fifth CSV file
file5_path = 'titanic_name_deanonymized.csv'
columns_file5 = ['name']
df5 = pd.read_csv(file5_path)

# Read the sixth CSV file
file6_path = 'titanic_deanonymise_randomization within class.csv'
columns_file6 = ['class']
df6 = pd.read_csv(file6_path)

# Select the desired columns from each dataframe
selected_columns_file1 = df1[columns_file1]
selected_columns_file2 = df2[columns_file2]
selected_columns_file3 = df3[columns_file3]
selected_columns_file4 = df4[columns_file4]
selected_columns_file5 = df5[columns_file5]
selected_columns_file6 = df6[columns_file6]

# Combine the selected columns into a new dataframe
result_df = pd.concat([selected_columns_file1, selected_columns_file2, selected_columns_file3, selected_columns_file4, selected_columns_file5, selected_columns_file6], axis=1)

# Write the result to a new CSV file
result_csv_path = 'titanic_deanonymized.csv'
result_df.to_csv(result_csv_path, index=False)

print("New CSV file created successfully.")