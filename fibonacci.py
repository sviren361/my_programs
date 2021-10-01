n=int(input("Enter no.s of terms "))
a1,a2=0,1
count=0
if n==1:
    print(a1)
else:
    while count<n:
        print(a1,end=" ")
        s=a1+a2
        a1=a2
        a2=s
        count=count+1