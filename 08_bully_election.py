import csv

alive = []

with open("bully_cluster_2.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        if r[1] == "TRUE":
            alive.append(int(r[0]))

        if r[2] == "TRUE" and r[1] == "FALSE":
            print("Coordinator failed:", r[0])

start = int(input("Enter initiating node: "))

for n in alive:
    if n > start:
        print("ELECTION:", n)
        print("OK:", n)

leader = max(alive)
print("COORDINATOR:", leader)
