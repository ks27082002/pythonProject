# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # temperature = []
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # print(data.to_dict())
#
# print(int(data[data.temp == max(data.temp)].temp))
# data.to_csv("new_data.csv")

import pandas, collections

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"])
dict = collections.defaultdict(int)
for color in data["Primary Fur Color"]:
    if color == "Gray" or color == "Cinnamon" or color == "Black":
        dict[color] += 1

print(dict.items())

dic = {}
dic["number"] = dict.values()
dic["color"] = dict.keys()
data_frame = pandas.DataFrame(dic)
data_frame.to_csv("new_squirrel_data.csv")