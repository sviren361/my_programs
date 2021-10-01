def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
v=int(input("Enter a number "))
l=len(str(v))
list=[]
for item in str(v):
    list.append(int(item))
# print(list)
s=[]
for item in list:
    x=fact(int(item))
    s.append(x)
# print(s)
if sum(s)==v:
    print(v,"is a strong number")
else:
    print(v,"is not a strong number")