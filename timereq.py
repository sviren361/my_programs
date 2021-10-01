name = str(input())
agent = int(input())
customer = str(input())
x = customer.split()
x.append(name)
x.sort()
number = x.index(name)
time = int((number//agent)*20)+20
print(time)
