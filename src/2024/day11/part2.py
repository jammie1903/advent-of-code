import sys

class QuantumSet:
  _instances = {}

  def __new__(cls, startingValue):
    # Check if an instance with the given value already exists
    if startingValue in cls._instances:
      return cls._instances[startingValue]
    # Create a new instance if it doesn't exist
    instance = super().__new__(cls)
    cls._instances[startingValue] = instance
    return instance

  def __init__(self, startingValue):
    # Only initialize if the instance is new
    if not hasattr(self, "_initialized"):
      self._startingValue = startingValue
      self._pointers = None
      self._blinkCounts = []
      self._initialized = True  # Prevent reinitialization

  def blink(self):
    count = 0
    if self._pointers == None:
      self._pointers = []
      if self._startingValue == "0":
        self._pointers.append(QuantumSet("1"))
      elif len(self._startingValue) % 2 == 0:
        # double slash == integer division
        halfPoint = len(self._startingValue) // 2
        self._pointers.append(QuantumSet(str(int(self._startingValue[:halfPoint]))))
        self._pointers.append(QuantumSet(str(int(self._startingValue[halfPoint:]))))
      else:
        self._pointers.append(QuantumSet(str(int(self._startingValue) * 2024)))
      count = len(self._pointers)
    else:
      for pointer in self._pointers:
        count += pointer.getCountAtBlink(len(self._blinkCounts))
    self._blinkCounts.append(count)
    return count

  def getCountAtBlink(self, index):
    if index == 0:
      return 1
    self.blinkTo(index)
    return self._blinkCounts[index - 1]

  def blinkTo(self, index):
    while index > len(self._blinkCounts):
      self.blink()


content = sys.argv[1]

values = content.split()

quantumPointers = [QuantumSet(s) for s in values]

blinkCount = 75

total = 0

for pointer in quantumPointers:
  total += pointer.getCountAtBlink(blinkCount)

print(total)
