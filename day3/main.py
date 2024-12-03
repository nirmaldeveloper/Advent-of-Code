import re
from typing import Pattern

input = ""

with open("input.csv", "r") as f:
  input = f.read()

f.close()
#part 1
total_sum =0
def findPattern(input):
  sum = 0
  pattern_match = r"mul\((\d+)\,(\d+)\)"
  output = re.findall(pattern_match, input)
  
  for i in output:
    sum += int(i[0]) * int(i[1])
  return sum

total_sum += findPattern(input)
print(total_sum)


#part 2
total_conditional_sum = 0
d= "don't"
input_split = input.split(d)
total_conditional_sum += findPattern(input_split[0])
for i in range(1, len(input_split)):
  #This string can be split on do alone as the don't is already split
  input_do_split = input_split[i].split("do")
  for j in range(1, len(input_do_split)):
    total_conditional_sum += findPattern(input_do_split[j])
print(total_conditional_sum)
