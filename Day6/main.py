import re
import math
input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

input_real = ""

with open("input.csv", "r") as f:
  input_real = f.read()

#Part 1
visits_count = 0
current_x_pos = 0
current_y_pos = 0 
loc_visited=[]
inputs = input_real.split("\n")


def getCurrentPOS(visits):
  for y in range(0, len(inputs)):
    for x in range(0, len(inputs[y])):
      if inputs[y][x] == "^":
        inputs[y] = inputs[y].replace("^",".")
        if([x,y] not in loc_visited):
          loc_visited.append([x,y])
          visits += 1
        return x, y, visits

def moveLeftTillObstructed(x, y, visits):
   obstructed = False
   while obstructed is False and x > 0:
     #Move Left
     x -= 1
     if inputs[y][x] == ".":
       if([x,y] not in loc_visited):
         loc_visited.append([x,y])
         visits +=1
     else:
       obstructed = True
       #Move Up Till Obstructed
       x+=1
       x, y, visits = moveUpTillObstructed(x,y, visits)
   return x, y, visits 

def moveDownTillObstructed(x, y, visits):
   obstructed = False
   while obstructed is False and len(inputs) - (y+1) > 0:
     #Move Down
     y += 1
     if inputs[y][x] == ".":
       if([x,y] not in loc_visited):
         loc_visited.append([x,y])
         visits +=1
     else:
       obstructed = True
       #Move Left Till Obstructed
       y -=1
       x, y, visits = moveLeftTillObstructed(x,y, visits)
   return x, y, visits 

def moveRightTillObstructed(x, y, visits):
   obstructed = False
   while obstructed is False and len(inputs[y]) - (x+1) > 0:
     #Move Right
     x += 1
     if inputs[y][x] == ".":
       if([x,y] not in loc_visited):
         loc_visited.append([x,y])
         visits +=1
     else:
       obstructed = True
       #Move Down Till Obstructed
       x -= 1
       x, y, visits = moveDownTillObstructed(x,y, visits)
   return x, y, visits 

def moveUpTillObstructed(x, y, visits):
   obstructed = False
   while obstructed is False and y > 0:
     #Move Up
     y -= 1
     if inputs[y][x] == ".":
       if([x,y] not in loc_visited):
         loc_visited.append([x,y])
         visits +=1
     else:
       obstructed = True
       #Move Right Till Obstructed
       y += 1 #Move one line Down
       x, y, visits = moveRightTillObstructed(x,y, visits)
   return x, y, visits   

current_x_pos, current_y_pos, visits_count = getCurrentPOS(visits_count)
current_x_pos, current_y_pos, visits_count = moveUpTillObstructed(current_x_pos, current_y_pos, visits_count)
print(visits_count)

#Part 2

