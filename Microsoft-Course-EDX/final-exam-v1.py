!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1.txt
def get_names() :
    while True :
        if(len(input_list) < 5):
            input_string = input("Enter the name of an element: ").strip().lower()
            if not input_string :
                continue
            elif (input_string not in input_list) :
                input_list.append(input_string)
            elif(input_string in input_list) :
                print(input_string,"was already entered <--no duplicates allowed")
        else :
            break
    return input_list;

fh = open('elements1.txt','r')
input_list =[]
index = 0
file_list =[]
Found_list =[]
Found_not_list =[]
file_string = fh.readline().strip("\n").upper().lower()
get_names()
while file_string :
    if file_string is None :
        break
    else :
        file_list.append(file_string)
        file_string = fh.readline().strip("\n").upper().lower()
fh.close()
for input_line in range(len(input_list)) :
    temp_comp=input_list[input_line]
    if  temp_comp in file_list :
        Found_list.append(input_list[input_line])
    else :
        Found_not_list.append(input_list[input_line])
correct_ans = int(len(Found_list))*20
print (correct_ans," %"," correct")
print("Found : ",' '.join(Found_list).title())
print("Not Found: ",' '.join(Found_not_list).title())
