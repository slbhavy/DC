import csv

workers = ["W1", "W2", "W3"]
load = [0, 0, 0]
jobs = [0, 0, 0]
i = 0

mode = "RR"  # Change to "LC" for Least Connections

with open("workload_5.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        if mode == "RR":
            w = i % 3
        elif mode == "LC":
            w = jobs.index(min(jobs))

        load[w] += int(r[1])
        jobs[w] += 1

        print(r[0], "assigned to", workers[w])
        print("Current Load:", load)

        i += 1

print("Final Load:", load)
