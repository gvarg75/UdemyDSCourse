student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic = {row.letter: row.code for (_,row) in df.iterrows()}
#print(phonetic)
#2. Create a list of the phonetic code words from a word that the user inputs.
all_letters = False
while not all_letters:
    name = input("What is your name?").upper()

    try:
        phone_list = [phonetic[letter] for letter in name]
        
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        print(phone_list)
        all_letters = True