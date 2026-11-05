import csv

times = []

with open("node_clocks_3.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        if r[2] == "FALSE":
            times.append([r[0], int(r[1])])
        else:
            print("Faulty node:", r[0])

avg = sum(x[1] for x in times) / len(times)

master = times[0][1]
avg_offset = avg - master

print("Average Clock Time:", avg)
print("Average Offset:", avg_offset)

for x in times:
    print(x[0], "Adjustment:", avg - x[1])
