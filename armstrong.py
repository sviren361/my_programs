while(True):
    try:
        n=input("Enter number : ")
        l=len(n)
        lis=list(n)
       
        arm=0
        for item in lis:
            arm+=int(item)**l
            
        if arm==int(n):
            print(f"{n} is an armstrong number")
        else:
            print(f"{n} is not an armstrong number")

    except ValueError:
        print("Enter valid number")