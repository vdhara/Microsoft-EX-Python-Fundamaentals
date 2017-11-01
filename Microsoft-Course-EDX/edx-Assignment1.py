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
            word = ""

if word.lower() >= "h":
    print("\n", word.upper())
