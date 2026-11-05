import csv
import threading

A = []

with open("matrix_22.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        A.append([int(x) for x in r[1:]])

n = len(A)
C = [[0] * n for i in range(n)]

def work(i):
    print("Worker:", i)

    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * A[k][j]

threads = []

print("MASTER SCATTERING")

for i in range(n):
    t = threading.Thread(target=work, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("MASTER GATHERING")
print(C)
