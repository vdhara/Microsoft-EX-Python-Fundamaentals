"""
[ ] initialize a list with several strings at the beginning of the program flow and follow the flow chart and output examples

example input/output

look at all the animals ['cat', 'goat', 'cat']
enter the name of an animal: horse
1 instance of horse appended to list

look at all the animals ['cat', 'goat', 'cat', 'horse']
enter the name of an animal: cat
1 instance of cat removed from list

look at all the animals ['goat', 'cat', 'horse']
enter the name of an animal: cat
1 instance of cat removed from list

look at all the animals ['goat', 'horse']
enter the name of an animal:          (<-- entered empty string)
horse popped from list

look at all the animals ['goat']
enter the name of an animal:          (<-- entered empty string)
goat popped from list

Goodbye!
example 2

look at all the animals ['cat', 'goat', 'cat']
enter the name of an animal: Quit
Goodbye!
"""

def list_o_matic(string_input,Animals) :
    if not string_input :
        pop_name = Animals.pop()
        print (pop_name,"popped from list")
        return ;
    elif (string_input in Animals):
        remove_name = Animals.remove(string_input)
        print ("1 instance of ",string_input," removed from list")
        return ;
    else :
        Animals.append(string_input)
        print("1 instance of",string_input,"appended to list")
        return ;
Animals = []
subtotal = 0
while True :
    raw_input =  input("please enter the  Animals name you want : ")
    if(raw_input != "Done"):
        Animals.append(raw_input.lower())
    else :
        break
if (len(Animals)!=0):
     while True :
         print("Look at all the Animals ",Animals)
         string_input =  input("enter the name of an animal : ")
         if(string_input != "Quit"):
             list_o_matic(string_input.lower(),Animals)
         else :
             break
 else:
     sys.exit()
