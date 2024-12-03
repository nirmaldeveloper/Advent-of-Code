import re

input = ""

with open("input.csv", "r") as f:
  input = f.read()

f.close()
sum =0
pattern_match = r"mul\((\d+)\,(\d+)\)"
output = re.findall(pattern_match, input)

for i in output:
  sum += int(i[0]) * int(i[1])
print(sum)
