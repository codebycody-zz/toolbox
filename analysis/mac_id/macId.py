import sys

print(sys.argv[1])

#open file
with open('oui.txt') as f:
    lines = f.readlines()

for line in lines:
    if line.split(' ')[0] == sys.argv[1]:
        print(line.rstrip('\n'))
        exit()
