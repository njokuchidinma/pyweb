import re
hand = open("regex-sum_assignment.txt")
digilist = list()
for line in hand:
    line = line.rstrip()
    deets = re.findall('[0-9]+', line)
    for deet in deets:
        digilist.append(int(deet))

print(sum(digilist))
