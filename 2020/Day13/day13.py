file1 = open('input13.txt', 'r')
Lines = file1.readlines()

startTime = 0
busID = []
earliestBusID = 0
earliestBudIDTimeDiff = 100


def populateFromFile():
    global busID
    global startTime

    for line in Lines:
        ids = []
        if(startTime == 0):
            startTime = int(line.strip())
        else:
            busID = line.strip().split(',')
            for id in busID:
                if(id != 'x'):
                    ids.append(id)
            busID = ids


def process():
    global busID
    global startTime
    global earliestBusID
    global earliestBudIDTimeDiff

    for id in busID:
        departTimes = 0
        while(departTimes < startTime):
            departTimes += int(id)

        if (departTimes - startTime < earliestBudIDTimeDiff):
            earliestBusID = int(id)
            earliestBudIDTimeDiff = departTimes - startTime


populateFromFile()
process()

print("Part 1 - answer:", earliestBusID*earliestBudIDTimeDiff)

with open('input13.txt') as f:
    arrival = int(next(f))
    ids = next(f).strip().split(',')

ids = [0 if id == 'x' else int(id) for id in ids]
departure = arrival

incr, t = 1, 0
for dt, id in zip([ids.index(i) for i in ids if i], [i for i in ids if i]):
    while (dt + t) % id:
        t += incr
    incr *= id

print("Part 2 - answer:", t)
