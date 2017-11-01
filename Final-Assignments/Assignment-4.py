"""
Create a program that:

imports and opens a file
appends additional data to a file
reads from the file to displays each city name and month average high temperature in Celsius
Output: The output should resemble the following

City of Beijing month ave: highest high is 30.9 Celsius
City of Cairo month ave: highest high is 34.7 Celsius
City of London month ave: highest high is 23.5 Celsius
City of Nairobi month ave: highest high is 26.3 Celsius
City of New York City month ave: highest high is 28.9 Celsius
City of Sydney month ave: highest high is 26.5 Celsius
City of Tokyo month ave: highest high is 30.8 Celsius
City of Rio De Janeiro month ave: highest high is 30.0 Celsius
all of the above text output is generated from the file
the only strings are hard coded:

"is"
"of"
"Celsius"
"""
!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp7.txt
temp_file = open('mean_temp7.txt','a+')
temp_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")
temp_file.seek(0,0)
headings = temp_file.readline()
headings = headings.split(',')
city_temp = temp_file.readline()
while city_temp:
    city_temp = city_temp.split(',')
    print(headings[0].title(),"of",city_temp[0],headings[2],"is",city_temp[2],"Celsius.")
city_temp = temp_file.readline() temp_file.close()
