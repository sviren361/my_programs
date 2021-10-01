import string
import random


a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.digits
d=string.punctuation

content=[]
content.extend(a)
content.extend(b)
content.extend(c)
content.extend(d)
while(True):
    random.shuffle(content)
    try :
        len=int(input("Enter the length of password : "))
        x="".join(content[0:len])
        print(x)
    
        print("Your strongest password is :")
    
        print("Thanks for using our password generator")
   
        with open ('passwords.txt','a') as f:
            f.write(x)
    except Exception as e:
        print("Enter valid credentials")