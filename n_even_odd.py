n=int(input("Enter a number "))
print(f"\nFirst {n} Even no.s \n")
for i in range(0,(2*n)):
    if i%2==0:
        print(i)
print("\n")
print(f"First {n} Odd no.s\n")
for j in range(0,(2*n+1)):
    if j%2!=0:
        print(j)

