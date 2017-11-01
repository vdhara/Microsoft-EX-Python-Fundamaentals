def word_mixer(Words_list) :
    Words_list.sort()
    print (Words_list,"\n")
    print ("Length of the word list is ",len(Words_list))
    while(len(Words_list) > 5) :
        Fifth_word = Words_list.pop(len(Words_list)-5)
        New_words.append(Fifth_word)
        First_word = Words_list.pop(0)
        New_words.append(First_word)
        Last_word = Words_list.pop()
        New_words.append(Last_word)
    return New_words;
Words_list = []
New_words = []
subtotal = 0
raw_input =  input("please enter the  poem line that you want : ")
Words_list = raw_input.split()
Words_length = len(Words_list)
for i  in range(Words_length) :
    if(len(Words_list[i])<= 3) :
        Words_list[i]=Words_list[i].lower()
    elif(len(Words_list[i])>= 7) :
        Words_list[i]=Words_list[i].upper()
word_mixer(Words_list)
