p=int(input("Enter a number "))
if p==0 or p==1:
    print("It is not prime")
for x in range(2,p):
    if p%x==0:
        print("It is not Prime")
        break
    else:
        print("It is Prime")
        break