"""
Program: Element_Quiz

In this program the user enters the name of any 5 of the first 20 Atomic Elements and is given a grade and test report for items correct and incorrect.

Sample input and output:

list any 5 of the first 20 elements in the Period table
Enter the name of an element: argon
Enter the name of an element: chlorine
Enter the name of an element: sodium
Enter the name of an element: argon
argon was already entered          <--no duplicates allowed
Enter the name of an element: helium
Enter the name of an element: gold

80 % correct
Found: Argon Chlorine Sodium Helium
Not Found: Gold
Create get_names() Function to collect input of 5 unique element names

The function accepts no arguments and returns a list of 5 input strings (element names)
define a list to hold the input
collect input of a element name
if input it is not already in the list add the input to the list
don't allow empty strings as input
once 5 unique inputs return the list
Create the Program flow

import the file into the Jupyter Notebook environment

use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt as elements1_20.txt
open the file with the first 20 elements
read one line at a time to get element names, remove any whitespace (spaces, newlines) and save each element name, as lowercase, into a list
Call the get_names() function

the return value will be the quiz responses list
check if responses are in the list of elements

Iterate through 5 responses

compare each response to the list of 20 elements
any response that is in the list of 20 elements is correct and should be added to a list of correct responses
if not in the list of 20 elements then add to a list of incorrect responses
calculate the % correct

find the the number of items in the correct responses and divide by 5, this will result in answers like 1.0, .8, .6,...
to get the % multiple the calculated answer above by 100, this will result in answers like 100, 80, 60...
hint: instead of dividing by 5 and then multiplying by 100, the number of correct responses can be multiplied by 20
Print output

print the Score % right
print each of the correct responses
print each of the incorrect responses
# [ ] create Element_Quiz
# then PASTE THIS CODE on then following page
"""

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
