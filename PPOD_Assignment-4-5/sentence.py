import pandas as pd

# Load the Titanic dataset
titanic_df = pd.read_csv('titanic.csv')

# Open a text file for writing with utf-8 encoding
with open('sentences.txt', 'w', encoding='utf-8') as file:
    # Iterate through each row
    for index, row in titanic_df.iterrows():
        # Extract information from the row
        name = row['name']
        country = row['country']
        gender = row['gender']
        age = row['age']
        ticket_number = row['ticketno']
        fare = row['fare']
        survived = 'survived' if row['survived'] == 1 else 'did not survive'

        # Create a sentence for each passenger
        sentence = f"{name}, a {country} citizen, was a passenger on the Titanic. "
        sentence += f"He was a {gender}, {age} years of age, traveled on the Titanic with ticket number {ticket_number} and paid a fare of ${fare}. "
        sentence += f"He {survived} the crash."

        # Write the sentence to the file
        file.write(sentence + '\n\n')
