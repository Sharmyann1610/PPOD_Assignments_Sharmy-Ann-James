import pandas as pd

# Read the first CSV file
file1_path = 'output_task.csv'
columns_file1 = ['manner_of_death', 'armed', 'signs_of_mental_illness', 'threat_level', 'flee', 'body_camera','is_geocoding_exact']
df1 = pd.read_csv(file1_path)

# Read the second CSV file
file2_path = 'deanonymized_output_task_date.csv'
columns_file2 = ['city']
df2 = pd.read_csv(file2_path)

# Read the third CSV file
file3_path = 'deanonymized_output_task_age.csv'
columns_file3 = ['age']
df3 = pd.read_csv(file3_path)

# Read the fourth CSV file
file4_path = 'deanonymized_output_task_city.csv'
columns_file4 = ['city']
df4 = pd.read_csv(file4_path)

# Read the fifth CSV file
file5_path = 'deanonymized_output_task_gender.csv'
columns_file5 = ['gender']
df5 = pd.read_csv(file5_path)

# Read the sixth CSV file
file6_path = 'deanonymized_output_task_location.csv'
columns_file6 = ['longitude', 'latitude']
df6 = pd.read_csv(file6_path)

# Read the seventh CSV file
file7_path = 'deanonymized_output_task_race.csv'
columns_file7 = ['race']
df7 = pd.read_csv(file7_path)

# Read the eighth CSV file
file8_path = 'deanonymized_output_task_state.csv'
columns_file8 = ['state']
df8 = pd.read_csv(file8_path)

# Read the nineth CSV file
file9_path = 'retrieved_name_id.csv'
columns_file9 = ['name','id']
df9 = pd.read_csv(file9_path)

# Select the desired columns from each dataframe
selected_columns_file1 = df1[columns_file1]
selected_columns_file2 = df2[columns_file2]
selected_columns_file3 = df3[columns_file3]
selected_columns_file4 = df4[columns_file4]
selected_columns_file5 = df5[columns_file5]
selected_columns_file6 = df6[columns_file6]
selected_columns_file7 = df7[columns_file7]
selected_columns_file8 = df8[columns_file8]
selected_columns_file9 = df9[columns_file9]

# Combine the selected columns into a new dataframe
result_df = pd.concat([selected_columns_file1, selected_columns_file2, selected_columns_file3, selected_columns_file4, selected_columns_file5, selected_columns_file6, selected_columns_file7, selected_columns_file8, selected_columns_file9], axis=1)

# Write the result to a new CSV file
result_csv_path = 'output_task_deanonymized.csv'
result_df.to_csv(result_csv_path, index=False)

print("New CSV file created successfully.")