import re
import math
input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
input_real = ""

with open("input.csv", "r") as f:
  input_real = f.read()
  
#Part 1
total_sum =0
page_input_with_updates = input.split("\n\n")
page_order = page_input_with_updates[0]
page_updates = page_input_with_updates[1].split("\n")
print_order = []
middle_updates = []
correct_pages = []
corrected_incorrect_pages = []
page_orders = page_order.split("\n")
def checkValidPage(page_current):
  current_updates = page_current.split(",")
  for i in range(0, len(current_updates)-1):
    for j in range(i+1, len(current_updates)):
      current = current_updates[j] + "|" + current_updates[i]
      #Check Anti-pattern
      if current in page_order:
        return False
  return True
def correctInvalidPage(page_incorrect):
  current_updates = page_incorrect.split(",")
  for i in range(0, len(current_updates)-1):
    for j in range(i+1, len(current_updates)):
      current = current_updates[j] + "|" + current_updates[i]
      #Check Anti-pattern
      temp =current_updates[i]
      #Swap if Anti-Pattern - re-arranging
      if current in page_order:
        current_updates[i] = current_updates[j]
        current_updates[j] = temp
        pass
      pass
    pass
  return ",".join(current_updates)    
    

for pages in page_updates:
  if checkValidPage(pages):
    correct_pages.append(pages)
  else:
    corrected_page = correctInvalidPage(pages)
    if checkValidPage(corrected_page):
      corrected_incorrect_pages.append(corrected_page)

for update in correct_pages:
  updates = update.split(",")
  middle_updates.append(int(updates[math.floor(len(updates)/2)]))

total_sum = sum(middle_updates)

corrected_middle_updates = []
for update in corrected_incorrect_pages:
  updates = update.split(",")
  corrected_middle_updates.append(int(updates[math.floor(len(updates)/2)]))

print(total_sum)

#Part 2
total_corrected_sum = sum(corrected_middle_updates)
print(total_corrected_sum)
