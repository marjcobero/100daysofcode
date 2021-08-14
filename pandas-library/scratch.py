import csv


# To read our data from our csv file
# hard coded
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":  # To get all the temperatures into a list of integers instead of a string
#            temperatures.append(int(row[1])) 
#    print(temperatures)


# better formatting for a csv file or to work with csv data
import pandas


data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# To calculate the average
average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

# to get the max value
print(data["temp"].max())

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# converting the temp from celsius to fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") # converts to a csv file and makes a new file