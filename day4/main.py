import re
input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
input_real = ""

with open("input.csv", "r") as f:
  input_real = f.read()

f.close()

#Part 1
total_sum =0
#Distance has to be atleast 3 top and bottom, diagonally left and right
def checkBottomLeftBound(currentIndexDis, lenBelow):
    return (currentIndexDis > 2 and lenBelow > 2)

def checkBottomRightBound(currentIndexDis, lenBelow):
    return (currentIndexDis > 2 and lenBelow > 2)

def checkTopLeftBound(currentIndexDis, lenAbove):
    return (currentIndexDis > 2 and lenAbove > 2)
    
def checkTopRightBound(currentIndexDis, lenAbove):
    return (currentIndexDis > 2 and lenAbove > 2)
def checkBottom(total, currentIndex):
   return ((total - (currentIndex + 1)) > 2)
def checkTop(currentIndex):
   return (currentIndex > 2)   
def checkLeft(currentIndex):
   return (currentIndex > 2)
def checkRight(currentIndexDis):
   return (currentIndexDis > 2)   
def findXYPattern(input):
  output_lines = input.split("\n")
  sum = 0
  diagonal_sum = 0
  for a in range(0, len(output_lines)):
      output_X = [ i for i,x in enumerate(output_lines[a]) if x == 'X']
      for x in output_X:
        #print("current", a, x)
        if(checkBottom(len(output_lines), a)):
           #print("Bottom", len(output_lines), a)
           if(output_lines[a+1][x] == "M" and output_lines[a+2][x] == "A" and output_lines[a+3][x] == "S"):
                #print("Bottom",a, x, output_lines[a+1][x], output_lines[a+2][x], output_lines[a+3][x])
                sum+=1
        if (checkTop(a)):
           #print("Top", len(output_lines), a)
           if(output_lines[a-1][x] == "M" and output_lines[a-2][x] == "A" and output_lines[a-3][x] == "S"):
                #print("Top",a, x, output_lines[a-1][x], output_lines[a-2][x], output_lines[a-3][x])
                sum+=1
        if(checkLeft(x)):
           #print("Left", len(output_lines), a)
           if(output_lines[a][x-1] == "M" and output_lines[a][x-2] == "A" and output_lines[a][x-3] == "S"):
                #print("Left",a, x, output_lines[a][x-2], output_lines[a][x-2], output_lines[a][x-3])
                sum+=1
        if (checkRight(len(output_lines[a])-(x+1))):
           #print("Right", len(output_lines), a)
           if(output_lines[a][x+1] == "M" and output_lines[a][x+2] == "A" and output_lines[a][x+3] == "S"):
                #print("Right",a, x, output_lines[a][x+1], output_lines[a][x+2], output_lines[a][x+3])
                sum+=1
        if(checkBottomLeftBound(x, len(output_lines[a]) - (a+1))):
            #print("BottomLeftBound",a, x, output_lines[a+1][x-1]+output_lines[a+2][x-2]+output_lines[a+3][x-3])
            if(output_lines[a+1][x-1] == "M" and output_lines[a+2][x-2] == "A" and output_lines[a+3][x-3] == "S"):
                #print("BottomLeftBound",a, x, output_lines[a+1][x-1], output_lines[a+2][x-2], output_lines[a+3][x-3])
                diagonal_sum += 1
                sum+=1
        if(checkBottomRightBound(len(output_lines[a]) -(x+1), len(output_lines) - (a+1))):
            #print("BottomRightBound",a, x, output_lines[a+1][x+1]+output_lines[a+2][x+2]+output_lines[a+3][x+3])
            if(output_lines[a+1][x+1] == "M" and output_lines[a+2][x+2] == "A" and output_lines[a+3][x+3] == "S"):
                #print("BottomRightBound",a, x, output_lines[a+1][x+1], output_lines[a+2][x+2], output_lines[a+3][x+3])
                diagonal_sum += 1
                sum+=1
        if(checkTopLeftBound(x, a)):
            #print("TopLeftBound",a, x, output_lines[a-1][x-1]+output_lines[a-2][x-2]+output_lines[a-3][x-3])
            if(output_lines[a-1][x-1] == "M" and output_lines[a-2][x-2] == "A" and output_lines[a-3][x-3] == "S"):
                #print("TopLeftBound",a, x, output_lines[a-1][x-1], output_lines[a-2][x-2], output_lines[a-3][x-3])
                diagonal_sum += 1
                sum+=1
        if(checkTopRightBound(len(output_lines[a]) -(x+1), a)):
            #print("TopRightBound",a, x, output_lines[a-1][x+1]+output_lines[a-2][x+2]+ output_lines[a-3][x+3])
            if(output_lines[a-1][x+1] == "M" and output_lines[a-2][x+2] == "A" and output_lines[a-3][x+3] == "S"):
                #print("TopRightBound",a, x, output_lines[a-1][x+1], output_lines[a-2][x+2], output_lines[a-3][x+3])
                diagonal_sum += 1
                sum+=1
  #print(diagonal_sum)
  return sum


total_sum += findXYPattern(input)
print(total_sum)

#Part 2
total_x_mass_sum = 0

word = "MAS"

def checkTopLeftBoundForA(currentLineIndex, charIndex):
    return currentLineIndex > 0 and charIndex > 0 
def checkTopRightBoundForA(currentLineIndex, charIndex, lineLen):
    return currentLineIndex > 0 and (lineLen - (charIndex +1)) > 0 
def checkBottomLeftBoundForA(currentLineIndex, charIndex, linesCount):
    return (linesCount - (currentLineIndex + 1)) > 0 and charIndex > 0 
def checkBottomRightBoundForA(currentLineIndex, charIndex, lineLen, linesCount):
    return (linesCount - (currentLineIndex + 1)) > 0 and (lineLen - (charIndex +1)) > 0
def topLeftChar(a):
    return a
def topRightChar(a):
    return a
def bottomLeftChar(a):
    return a
def bottomRightChar(a):
    return a

def findXPattern(input):
  output_lines = input.split("\n")
  sum = 0
  #print(len(output_lines))
  #Iterate line by line to check number of X-MAS from each line
  for a in range(0, len(output_lines)):
      pivot_char = "A"
      #Get index of A for each line from 1 to number of lines - 1
      #Changed it to get from all lines from 0 to len of number of lines - 1
      output_A = [i for i,x in enumerate(output_lines[a]) if x == pivot_char]
      for x in output_A:
        #check if X-MAS has a range for top-left, top-right, bottom-left, bottom-right and doesn't go out of range
        if(checkTopLeftBoundForA(a, x) and checkTopRightBoundForA(a, x, len(output_lines[a])) and checkBottomLeftBoundForA(a, x, len(output_lines)) and checkBottomRightBoundForA(a, x, len(output_lines[a]), len(output_lines))):
            #Four Edges scenario to check if M or S forms which opposite edges
            if(
               (topLeftChar(output_lines[a-1][x-1]) == "M" and topRightChar(output_lines[a-1][x+1]) == "M" 
               and bottomLeftChar(output_lines[a+1][x-1]) == "S" and bottomRightChar(output_lines[a+1][x+1])=="S")
               or 
               (topLeftChar(output_lines[a-1][x-1]) == "M" and bottomLeftChar(output_lines[a+1][x-1]) == "M" 
               and topRightChar(output_lines[a-1][x+1]) == "S" and bottomRightChar(output_lines[a+1][x+1])=="S")
               or
               (topLeftChar(output_lines[a-1][x-1]) == "S" and topRightChar(output_lines[a-1][x+1]) == "S" 
               and bottomLeftChar(output_lines[a+1][x-1]) == "M" and bottomRightChar(output_lines[a+1][x+1])=="M")
               or 
               (topLeftChar(output_lines[a-1][x-1]) == "S" and bottomLeftChar(output_lines[a+1][x-1]) == "S" 
               and topRightChar(output_lines[a-1][x+1]) == "M" and bottomRightChar(output_lines[a+1][x+1])=="M")):
                sum += 1
  return sum

total_x_mass_sum += findXPattern(input)
print(total_x_mass_sum)
