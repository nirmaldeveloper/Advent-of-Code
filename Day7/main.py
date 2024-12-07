import time
from itertools import permutations

startTime = time.perf_counter()
input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input_real = ""

with open("input.csv", "r") as f:
  input_real = f.read()

#Part 1
startTime = time.perf_counter()
def checkResult(i, inputResult, nums, cur, part):
    if i == len(nums) and cur == inputResult:
        return True
    if cur > inputResult or cur < 0 or i >= len(nums):
        return False
    if checkResult(i + 1, inputResult, nums, cur + nums[i], part):
        return True
    if checkResult(i + 1, inputResult, nums, cur * nums[i], part):
        return True
    if part == 2 and checkResult(i+1, inputResult, nums, int(str(cur) + "" + str(nums[i])),part):
        return True
    return False

def main():
    #Part 1
    startTime = time.perf_counter()
    answer = 0
    answerPartB = 0
    lines = input_real.split("\n")
    for line in lines:
      test_value, numbers = line.split(":")
      test_value = int(test_value.strip())
      nums = list(map(int, numbers.strip().split()))
      if checkResult(1, test_value, nums, nums[0], 1):
         answer += test_value
         pass
    endTime = time.perf_counter()
    print(f"Part 1 solved in {endTime - startTime}")
    #Part 2
    startTime = time.perf_counter()
    for line in lines:
      test_value, numbers = line.split(":")
      test_value = int(test_value.strip())
      nums = list(map(int, numbers.strip().split()))
      if checkResult(1, test_value, nums, nums[0], 2):
         answerPartB += test_value
         pass
      pass
    endTime = time.perf_counter()
    print(f"Part 2 solved in {endTime - startTime}")
    print(answer)
    print(answerPartB)


if __name__ == "__main__":
    main()








