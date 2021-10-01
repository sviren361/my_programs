s=[]
while True:
    n=int(input("Enter numbers "))
    if n==0:
        break
    s.append(n)
s.sort()
print(s)
l=[]
for i in range(len(s)):
    x=max(s)
    l.append(x)
    s.remove(x)
print(l)



