!curl  https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_text.txt
the_file = open("mean_temp.txt", "a+")
the_file.seek(0,2)
#the_file.write("\n")
the_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")
the_file.seek(0,0)
headings = the_file.readline().strip('\n').split(',')
city_temp = the_file.readline()
while city_temp:
    city_temp = city_temp.split(',')
    print(headings[0].title(),"of",city_temp[0],headings[2],"is",city_temp[2],"Celsius")
    city_temp = the_file.readline()
the_file.close()
