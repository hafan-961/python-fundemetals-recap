'''Generate random number
check  which numbers are even / odd
round numbers using math 
count how many times number appear
save the result in a file '''


import random
import math
import os
import re
from collections import Counter


numbers = [random.randint(1,10) for _ in range(10)] 
print(numbers)

#even or odd

even_numbers = []
odd_numbers = []

for num in numbers:
    nums_str = str(num)
    if re.search(r"^[02468]$" , nums_str):
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

#calculating average
average = sum(numbers)/len(numbers)
#round off the averag
rounded_avg = math.ceil(average)

count_numbers = Counter(numbers)

#save result using os

if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")
#file path
file_path = os.path.join("easy_repots", "number_report.txt")

#write data to a file
file = open(file_path,"w")
file.write(f"Generated numbers: {numbers}")
file.write(f"Even numbers: {even_numbers}")
file.write(f"Odd numbers: {odd_numbers}")
file.write(f"average: {rounded_avf}")
file.write(f"number count:\n")
for num,count in count_numbers.items():
    file.write(f"{num} : {count}\n")
file.close()


print(....)



    