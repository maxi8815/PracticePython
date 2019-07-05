
open_file = open('python.txt', 'r')
splitter = open_file.read().split()
howMuch = 0
for elements in splitter:
    howMuch = howMuch +1
print(howMuch)