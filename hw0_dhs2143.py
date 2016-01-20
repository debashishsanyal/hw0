#HW0, Intro to Database w111 - Evan Jones
#Due date 01/21/2016
#UNI dhs2143

import csv

count = 0
string = "single,malt,scotch"

with open('iowa-liquor-sample.csv', 'rb') as csvfile:
    read_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in read_file:
        temp1 = ','.join(row).lower()
        if string in temp1:
            count += 1

print str(count) + " records contain the phrase 'single malt scotch'."
