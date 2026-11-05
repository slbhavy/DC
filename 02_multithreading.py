import csv
import threading
import time

lock = threading.Lock()
done = []

def work(r):
    print("Starting:", r[1], r[0])
    time.sleep(int(r[2]) / 1000)

    with lock:
        print("Lock acquired:", r[1])
        done.append(r[0])

    print("Lock released:", r[1])

threads = []

with open("tasks_4.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        t = threading.Thread(target=work, args=(r,))
        t.start()
        threads.append(t)

for t in threads:
    t.join()

print("Completed tasks:", done)
