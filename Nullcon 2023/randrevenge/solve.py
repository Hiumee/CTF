# Make a post request to the server with the data "next=2"
import os
import requests
import csv

url = "http://52.59.124.14:10012/"

d = {}

i = 0

with open('data.csv') as csvfile:

    spamreader = csv.reader(csvfile)

    for row in spamreader:
        i+=1
        # check if in dict
        if i == 20796091:
            break
        if row[0] in d:
            d[row[0]].append(row[1])
        else:
            d[row[0]] = [row[1]]
            z = row[0]

print(f"Loaded {i} lines")

while True:
    r = requests.post(url)
    data = r.text.split("\n")

    data[0] # time
    leak = data[1]

    if leak in d:
        number = os.popen(f"php a.php {len(d[leak])} {' '.join(d[leak])} {' '.join(data[:-2])}").read()

        print(f"Number: {number}")

        cookies = r.cookies

        r = requests.post(url+"submit", data={"next": number}, cookies=cookies)
        print(r.text)
        if "ENO" in r.text:
            exit()