import csv

nodes = {}
active = []

with open("ring_nodes_15.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        nodes[int(r[0])] = int(r[1])

        if r[2] == "TRUE":
            active.append(int(r[0]))
        else:
            print("Discarding:", int(r[0]))

print("Coordinator failed:")

current = active[0]
visited = []

while current not in visited:
    visited.append(current)

    if current in active:
        print("Token:", current)

    current = nodes[current]

leader = max(active)
print("New Leader:", leader)
