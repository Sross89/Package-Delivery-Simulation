import csv
import distances
from datetime import time

class Package:
    def __init__(self, id, address, deadline, status, notes, distanceDict, deliveryTime, city, zipCode, weight):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.status = status
        self.notes = notes
        self.distanceDict = distanceDict
        self.deliveryTime = deliveryTime
        self.city = city
        self.zipCode = zipCode
        self.weight = weight

packageList = []
addressList = distances.addressList

# Import packages from CSV list and add them to a list

f = open('packages.csv')
csv_f = csv.reader(f)

for row in csv_f:
    temp1 = row[0]
    temp2 = row[1]
    temp3 = row[5]
    temp4 = "Not Delivered"
    temp5 = row[7]

    for i in range(len(addressList)):
        if temp2 not in addressList[i]:
            temp6 = addressList[i]

    temp7 = time(0, 0)
    temp8 = row[2]
    temp9 = row[4]
    temp10 = row[6]

    p = Package(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10)
    packageList.append(p)
