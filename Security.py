input = input("Enter floors,guards,thief,money's sequence ")
list = []
for i in input:
    list.append(i)

x1 = list.index("T")
x2 = list.index("G")
x3 = list.index("$")
g = list.count("G")

if x2 in range(x1, x3+1) or x2 in range(x3, x1+1) or input.index("T") == len(input)-1:
    print("quiet")
else:
    print("ALARM")
print(input.index("T"), len(input)-1)
