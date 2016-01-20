#Hw0 Intro to Databse w111 - Evan Jones
#Due date 01/21/2016
import csv

count = 0
string = "single,malt,scotch"
rows = 0
with open('iowa-liquor-sample.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        temp1 = ','.join(row).lower()
        if string in temp1:
            count += 1
        rows += 1

print str(count) + " 'single malt scotch' found."
