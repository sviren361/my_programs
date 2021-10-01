# def fibo(n):
#     if n==0 :
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

def fibiterate(n):
    prevNum=0
    currentNum=1
    for i in range(1,n):
        prevPrevNum=prevNum
        prevNum=currentNum
        currentNum=currentNum+prevPrevNum
    return currentNum


    
while True:
    num=int(input("Enter the nth no. "))
    # x=fibo(num)
    y=fibiterate(num)
    # print(f"The {num}th term of series is {x}")
    print(f"The {num}th term of series is {y}")
    