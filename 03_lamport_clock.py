import csv

events = []
clock = {}
messages = {}

with open("events_7.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        e, p, typ, dest, t = r
        t = int(t)

        if typ == "SEND":
            clock[p] = max(clock.get(p, 0), t) + 1
            messages[(p, dest)] = clock[p]

        elif typ == "RECEIVE":
            msg = messages.get((dest, p), 0)
            clock[p] = max(clock.get(p, 0), msg, t) + 1

        else:
            clock[p] = max(clock.get(p, 0), t) + 1

        events.append((clock[p], p, e))
        print(e, "Clock:", clock[p])

print("\nTotal Causal Order")

for t, p, e in sorted(events):
    print(e, "Timestamp:", t)
