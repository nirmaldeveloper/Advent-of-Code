
lst1 = []
lst2 = []

with open("input.csv", "r") as f:
  for line in f.readlines():
    input1, input2 = line.split()
    lst1.append(int(input1))
    lst2.append(int(input2))
  

lst1_sorted = sorted(lst1)
lst2_sorted =sorted(lst2)


sum = 0

for i in range(len(lst1)):
  sum += abs(lst1_sorted[i] - lst2_sorted[i])
  #print(lst1[i], lst2[i], abs(lst1[i] - lst2[i]))
print(sum)

count_sum = 0
for i in range(len(lst1_sorted)):
  count_sum += lst1_sorted[i] * lst2_sorted.count(lst1_sorted[i])

print(count_sum)
