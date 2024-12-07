import sys

content = sys.argv[1]

lines = content.splitlines()
total = 0

for line in lines:
  goal, numbersStr = line.split(":")
  numbers = [int(num) for num in numbersStr.split()]
  results = [numbers[0]]
  for number in numbers[1:]:
    oldResults = results
    results = []
    for result in oldResults:
      results.append(result + number)
      results.append(result * number)
  print(results)
  if int(goal) in results:
    total += int(goal)

print(total)
