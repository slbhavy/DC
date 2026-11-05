import csv

# RPC function
def processData(x):
    return x * 2

# RMI class
class Server:
    def processData(self, x):
        return x * 2

server = Server()

choice = input("Enter 1 for RPC or 2 for RMI: ")

with open("rpc_calls_1.csv") as f:
    data = csv.reader(f)
    next(data)

    for r in data:
        print("\n[DISPATCH] Client:", r[1])
        print("Method:", r[2])

        value = int(r[3])
        print("[SERVER EXECUTION] Processing:", value)

        if choice == "1":
            result = processData(value)
            print("[RPC]")
        elif choice == "2":
            result = server.processData(value)
            print("[RMI]")
        else:
            print("Invalid choice")
            break

        print("[RETURN] Result:", result)
