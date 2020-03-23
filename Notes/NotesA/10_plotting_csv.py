import csv

with open("../Libraries_-_2019_Visitors_by_Location (1).csv")as f:
    reader = csv.reader(f)
    data = list(reader)
names = [x[0]for x in data]
sulzer_index = names.index("Sulzer Regional Library")
sulzer_data = [sulzer_index]

sulzer_by_month = sulzer_data[3:1]