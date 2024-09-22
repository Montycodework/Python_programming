# import csv
#
# with open("weather_data (1).csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#     print("Lekin ek list extract krne ke liye ye kuch jyada hi lamba code he to hum ab seekhenge panda lib ka use")

# __________Pandas lib_______

import pandas

data  = pandas.read_csv("weather_data (1).csv")
# print(data)
print(data["temp"])
