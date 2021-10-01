EXCHANGE=(('A','@'),('V','\/'),('I','|'))
def secured(password):
    for a,b in EXCHANGE:
        password= password.replace(a,b)
    return password
               

password=input("Enter password ")
password=secured(password)
print(f"Your secured password is : {password}")
       