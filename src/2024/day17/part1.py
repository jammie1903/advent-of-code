import sys

content = sys.argv[1]

lines = content.splitlines()

stores = dict()

pointerLocation = 0

output = []

# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
def getComboOperand(operand):
  if operand >= 0 and operand <= 3:
    return operand
  elif operand == 4:
    return stores.get("A", 0)
  elif operand == 5:
    return stores.get("B", 0)
  elif operand == 6:
    return stores.get("C", 0)
  else:
    raise ValueError(f"Invalid operand: {operand}")

# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
def adv(operand):
  numerator = stores.get("A", 0)
  comboOperand = getComboOperand(operand)
  divisor = 2**comboOperand
  stores["A"] = int(numerator / divisor)

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
def bxl(operand):
  stores["B"] = operand ^ stores.get("B", 0)

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
def bst(operand):
  stores["B"] = getComboOperand(operand) % 8

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
def jnz(operand):
  global pointerLocation
  if stores.get("A", 0) != 0:
    # -2 to avoid having to prevent an increase of 2 outside of this function
    pointerLocation = operand - 2

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(operand):
  stores["B"] = stores.get("B", 0) ^ stores.get("C", 0)

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
def out(operand):
  output.append(str(getComboOperand(operand) % 8))

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
def bdv(operand):
  numerator = stores.get("A", 0)
  comboOperand = getComboOperand(operand)
  divisor = 2**comboOperand
  stores["B"] = int(numerator / divisor)

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
def cdv(operand):
  numerator = stores.get("A", 0)
  comboOperand = getComboOperand(operand)
  divisor = 2**comboOperand
  stores["C"] = int(numerator / divisor)

opcodeMap = {
  0: adv,
  1: bxl,
  2: bst,
  3: jnz,
  4: bxc,
  5: out,
  6: bdv,
  7: cdv,
}

def processInstruction(opcode, operand):
  opcodeMap.get(opcode, lambda x: print("Unknown opcode: " + str(x)))(operand)


for line in lines:
  if not ":" in line: continue
  key, value = line.split(":", 1)
  if key.startswith("Register "):
    register = key.split(" ")[1]
    stores[register] = int(value.strip())
  elif key == "Program":
    program = list(map(int, value.split(",")))
  else: print("Unknown key " + str(key))

while pointerLocation < len(program):
  opcode, operand = program[pointerLocation:pointerLocation+2]
  print("before", { "opcode": opcode, "operand": operand, "pointer": pointerLocation, "stores": stores })

  processInstruction(opcode, operand)
  pointerLocation += 2
  print("after", { "opcode": opcode, "operand": operand, "pointer": pointerLocation, "stores": stores })

print(",".join(output))
