def fact(n):
    if n==0 or n==1:
       return n
    else:
        return n* fact(n-1)
def trailing(n):
    count=0
    i=5
    while n/i!=0:
        count+=int(n/i)
        i+=5
        return count



while(True):
    try:
        x=int(input("Enter the number: "))
        fac=fact(x)
        trail=trailing(x)
        print(f"Factorial is {fac}")
        print(f"Trailing zeroes are {trail}")
    except ValueError:
        print("No. taak re")
    except RecursionError:
        print("Nako evda, rahude")
        