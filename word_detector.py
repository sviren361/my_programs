import os
def detect(text,filename):
    with open (filename,'r') as f:
        filecontent=f.read()
        if text in filecontent.lower():
            return True
        else:
            return False

while(True):
    text=input("Enter text to be searched : ")
    dir_content= os.listdir()
    for item in dir_content:
        if item.endswith('txt'):
            print(f"Scanning {item}")
            flag=detect(item)
            if (flag):
                print(f"{text} found")
            else:
                print(f"{text} not found")
