import pandas

NATO_df = pandas.read_csv("nato_phonetic_alphabet.csv")
user_input = input("Please enter word to be converted: ").upper()

NATO_dict = {row.letter: row.code for (index, row) in NATO_df.iterrows()}
return_list = [NATO_dict[letter] for letter in list(user_input)]

print(return_list)
