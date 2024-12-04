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
total_sum =0
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
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

#Part 1
total_sum += findXYPattern(input)
print(total_sum)

#Part 2

