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
