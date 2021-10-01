while True:

    print("Enter Sport name for Lots from Football, Cricket, Volleyball, Kabbadi, Khokho : ")
    s=input()
    import random
    import os
    if s=="Football":
        try:
            try:
                os.remove("\Practice\Football.txt")
            except: FileNotFoundError
            teams=['FY A','FY B','FY C','FY D','FY E','SY ECT','SY CST','SY Civil','SY Chemical','SY Mechanical','SY Food','TY ECT','TY CST','TY Civil','TY Chemical','TY Mechanical','TY Food','Final ECT','Final CST','Final Civil','Final Chemical','Final Mechanical','Final Food']
            winner=input("Enter current year of last year's winner : \n")
            teams.remove(winner)
            l=int((len(teams))/2)
            x=random.sample(teams,l)
             
            for items in x:

                teams.remove(items)

            for i in range(l):
                
                lots=(f"{x[int(i)]} vs {teams[int(i)]}\n\n\n")
                pr=list(lots) 
                print(lots)
                f=open('Football.txt', 'a')
                f.writelines(i for i in pr)

            f.write(f"{winner.upper()} (last year winners)\n\n")
            f.write(f"                      {s.upper()}\n\n")
            f.close()

        except ValueError:
            print("Enter Valid Team") 
    elif s=="Cricket":
        try:
            try:
                os.remove("\Practice\Cricket.txt")
            except: FileNotFoundError
            teams=['FY A','FY B','FY C','FY D','FY E','SY ECT','SY CST','SY Civil','SY Chemical','SY Mechanical','SY Food','TY ECT','TY CST','TY Civil','TY Chemical','TY Mechanical','TY Food','Final ECT','Final CST','Final Civil','Final Chemical','Final Mechanical','Final Food']
            winner=input("Enter current year of last year's winner : \n")
            teams.remove(winner)
            l=int((len(teams))/2)
            x=random.sample(teams,l)
             
            for items in x:

                teams.remove(items)
                
            for i in range(l):
                
                lots=(f"{x[int(i)]} vs {teams[int(i)]}\n\n\n")
                pr=list(lots) 
                print(lots)
                f=open('Cricket.txt', 'a')
                f.writelines(i for i in pr)

            f.write(f"{winner.upper()} (last year winners)\n\n")
            f.write(f"                      {s.upper()}\n\n")
            f.close()

        except ValueError:
            print("Enter Valid Team")
    elif s=="Kabbadi":
        try:
            try:
                os.remove("\Practice\Kabbadi.txt")
            except :
                FileNotFoundError

            teams=['FY A','FY B','FY C','FY D','FY E','SY ECT','SY CST','SY Civil','SY Chemical','SY Mechanical','SY Food','TY ECT','TY CST','TY Civil','TY Chemical','TY Mechanical','TY Food','Final ECT','Final CST','Final Civil','Final Chemical','Final Mechanical','Final Food']
            winner=input("Enter current year of last year's winner : \n")
            teams.remove(winner)
            l=int((len(teams))/2)
            x=random.sample(teams,l)
             
            for items in x:

                teams.remove(items)
                
            for i in range(l):
                
                lots=(f"{x[int(i)]} vs {teams[int(i)]}\n\n\n")
                pr=list(lots) 
                print(lots)
                f=open('Kabbadi.txt', 'a')
                f.writelines(i for i in pr)

            f.write(f"{winner.upper()} (last year winners)\n\n")
            f.write(f"                      {s.upper()}\n\n")
            f.close()

        except ValueError:
            print("Enter Valid Team")
    elif s=="KhoKho":
        try:
            try:
                os.remove("\Practice\Kabbadi.txt")
            except: FileNotFoundError
            teams=['FY A','FY B','FY C','FY D','FY E','SY ECT','SY CST','SY Civil','SY Chemical','SY Mechanical','SY Food','TY ECT','TY CST','TY Civil','TY Chemical','TY Mechanical','TY Food','Final ECT','Final CST','Final Civil','Final Chemical','Final Mechanical','Final Food']
            winner=input("Enter current year of last year's winner : \n")
            teams.remove(winner)
            l=int((len(teams))/2)
            x=random.sample(teams,l)
             
            for items in x:

                teams.remove(items)
                
            for i in range(l):
                
                lots=(f"{x[int(i)]} vs {teams[int(i)]}\n\n\n")
                pr=list(lots) 
                print(lots)
                f=open('KhoKho.txt', 'a')
                f.writelines(i for i in pr)

            f.write(f"{winner.upper()} (last year winners)\n\n")
            f.write(f"                      {s.upper()}\n\n")
            f.close()

        except ValueError:
            print("Enter Valid Team")
    elif s=="Volleyball":
        try:
            try:
                os.remove("\Practice\Volleyball.txt")
            except: FileNotFoundError
            teams=['FY A','FY B','FY C','FY D','FY E','SY ECT','SY CST','SY Civil','SY Chemical','SY Mechanical','SY Food','TY ECT','TY CST','TY Civil','TY Chemical','TY Mechanical','TY Food','Final ECT','Final CST','Final Civil','Final Chemical','Final Mechanical','Final Food']
            winner=input("Enter current year of last year's winner : \n")
            teams.remove(winner)
            l=int((len(teams))/2)
            x=random.sample(teams,l)
             
            for items in x:

                teams.remove(items)
                
            for i in range(l):
                
                lots=(f"{x[int(i)]} vs {teams[int(i)]}\n\n\n")
                pr=list(lots) 
                print(lots)
                f=open('Volleyball.txt', 'a')
                f.writelines(i for i in pr)

            f.write(f"{winner.upper()} (last year winners)\n\n")
            f.write(f"                      {s.upper()}\n\n")
            f.close()

        except ValueError:
            print("Enter Valid Team")        
    else:
        print("Enter Valid Sport Name")

