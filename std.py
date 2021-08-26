import csv
import math
import numpy as np
import pandas as pd
with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total / n
    return mean

squared_list = []
for n in data:
    a = int(n) - mean(data)   
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum += i

result = sum/(len(data)-1)
std = math.sqrt(result) 
print(std)