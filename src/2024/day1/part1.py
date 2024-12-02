import sys
content = sys.argv[1]

lines = content.splitlines()
arr1 = []
arr2 = []

for line in lines:
  val1, val2 =line.split()[:2]
  arr1.append(val1)
  arr2.append(val2)

arr1.sort()
arr2.sort()

total = 0

for index, value in enumerate(arr1):
  value2 = arr2[index]
  total += abs(int(value) - int(value2))

print("result", total)
sys.stdout.flush()
