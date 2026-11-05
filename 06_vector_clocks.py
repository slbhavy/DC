import csv

P = ["P1", "P2", "P3"]
V = [[0, 0, 0] for i in range(3)]
messages = {}
events = []

with open("vector_events_6.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        p = P.index(r[1])

        if r[2] == "SEND":
            V[p][p] += 1
            messages[(r[1], r[3])] = V[p][:]

        elif r[2] == "RECEIVE":
            msg = messages.get((r[3], r[1]), [0, 0, 0])

            for i in range(3):
                V[p][i] = max(V[p][i], msg[i])

            V[p][p] += 1

        else:
            V[p][p] += 1

        events.append([r[0], V[p][:]])
        print(r[0], "Vector:", V[p])

print("\nEvent Comparison:")

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        a = events[i][1]
        b = events[j][1]

        if all(a[k] <= b[k] for k in range(3)) and a != b:
            print(events[i][0], "Before", events[j][0])

        elif all(b[k] <= a[k] for k in range(3)) and a != b:
            print(events[j][0], "Before", events[i][0])

        else:
            print(events[i][0], "||", events[j][0], "Concurrent")
