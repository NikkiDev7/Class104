import csv
with open("SOCR-HeightWeight.csv") as data:
    reader = csv.reader(data)
    file_data = list(reader)

file_data.pop(0)
new_data = []

length = len(file_data)
for i in range(length):
    height = file_data[i][1]
    new_data.append(float(height))

#-----------MEAN---------
# avg = sum/total

total = len(new_data)
sum = 0

for i in new_data:
    sum = sum + i

mean = sum/total
print(f"Mean is {mean}")

#---------------MEDIAN---------
new_data.sort()
if total % 2 == 0: #even
    median1 = float(new_data[total//2])
    median2 = float(new_data[(total//2) -1])
    median = (median1 + median2) / 2  
else: #odd
    median = new_data[total//2]
print("Median is {}".format(median))

#----------------MODE------------------
from collections import Counter
mode_data = Counter(new_data)
mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

'''
niketh = {
    "job":"student",
    "location":"USA"
}

niketh["job"] = student
'''

for key,value in mode_data.items():
    if 50< float(key) <60:
       mode_data_for_range["50-60"] += value
    elif 60< float(key) <70:
       mode_data_for_range["60-70"] += value
    elif 70< float(key) <80:
       mode_data_for_range["70-80"] += value

        
mode_range = 0
mode_occuernce = 0
for i,occ in mode_data_for_range.items():
    if occ > mode_occuernce:
        mode_range, mode_occuernce = [int(i.split("-")[0]), int(i.split("-")[1])]

mode = float((mode_range[0] + mode_range[1])/2)
print(f' mode is {mode}')

