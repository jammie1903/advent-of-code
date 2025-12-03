import sys
content = sys.argv[1]

banks = content.split("\n")
total = 0

for bank in banks:
  max = 0
  for i in range(len(bank) - 1):
    iNum = int(bank[i]) * 10
    if (iNum < max): continue
    for j in range(i + 1, len(bank)):
      number = iNum + int(bank[j])
      if number > max:
        max = number
  total += max

print("result", total)
sys.stdout.flush()
