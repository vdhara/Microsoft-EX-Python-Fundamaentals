"""
Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z

Sample input:
enter a 1 sentence quote, non-alpha separate words: Wheresoever you go, go with all your heart

Sample output:
WHERESOEVER
YOU
WITH
YOUR
HEART
"""
#input from User
quote = input("Enter a 1 sentence quote, non - alpha seperate words: ")
word = ""
for character in quote:
    if character.isalpha():
        word = word + character
    else:
        if word and word[0].lower() >= "h":
            print(word.upper(),"\n")
            word = ""
        else:
            word = ""  if word.lower() >= "h":
            print("\n", word.upper())
