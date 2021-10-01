# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# i=int(input("Enter a number "))   #input for recursive function
# x=fact(i)
# print(x)

# Without recursion

m = int(input("Enter a number "))  # input for without recursion
f = 1
while(m > 0):
    f = f*m
    m = m-1
print("Factorial of the number is: ")
print(f)
