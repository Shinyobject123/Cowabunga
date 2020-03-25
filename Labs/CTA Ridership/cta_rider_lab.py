'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

import csv
import math
import matplotlib.pyplot as plt

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

# pop header
header = data.pop(0)

years = []
bNum = []
rNum = []
aNum = []

print(data[0])
for year in data:
    try:
        # get last 10 years
        yr = int(year[0])
        # decade check
        chk = math.sqrt(yr-2009)
        years.append(yr)
        # get last 10 years bus
        bus = float(year[1])
        bNum.append(bus)
        # get last 10 years rail
        rail = float(year[3])
        rNum.append(rail)
        # get last 10 years total
        all = bus + rail
        aNum.append(all)
    except:
        print("", end ="")
print(rNum)
print()
plt.figure("CTA", figsize=(6,5))

# plot bus
plt.plot(years, bNum, label="Bus")
# plot rail
plt.plot(years, rNum, label="Rail")
# plot total
plt.plot(years, aNum, label="Total")

# axis
plt.xlabel('Year')
plt.ylabel('Riders')
# title
plt.title('CTA Ridership')
# legend (label plots)
plt.legend()

# show plot
plt.show()













