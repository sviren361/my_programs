a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
x=max(a,b)
while(True):
    if x%a==0 and x%b==0:
        break
        
    x+=1
print(f"LCM is {x}")