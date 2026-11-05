import csv

with open("cristian_clocks_8.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        t0 = int(r[1])
        ts = int(r[2])
        t1 = int(r[3])

        rtt = t1 - t0
        correct = ts + rtt / 2
        offset = correct - t1

        print("Client:", r[0])
        print("RTT:", rtt)
        print("Server Time:", correct)
        print("Offset:", offset)
        print("Adjusted Time:", t1 + offset)
