a=int(input("Enter first no. "))
b=int(input("Enter second no. "))
c=int(input("Enter third no. "))
x=max(a,b,c)
while(True):
    if x%a==0 and x%b==0 and x%c==0:
        break
    x+=1
print("LCM of",a,b,c,"is",x)


y=min(a,b,c)
for i in range(1,y+1):
    if a%i==0 and b%i==0 and c%i==0:
        hcf=i
print("HCf of",a,b,c,"is",hcf)
