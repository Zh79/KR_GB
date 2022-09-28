m = ["hello", "2", "world", ":-)"]
m = ["1234", "1567", "-2", "computer science"]
m = ["Russia", "Denmark", "Kazan"]
newM = []

for n in range(len(m)):
    if len(m[n]) <= 3:
        newM.append(m[n])

for m in range(len(newM)):
    print(newM[m])

