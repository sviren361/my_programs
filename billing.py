menu={'Misal':40,'Pohe':20,'Upama':20,'Sheera':20,'Dosa':30,'Uttapa':40,'Vadapav':20,'Tea':10,'Special':20}
s=0
x=[]
q=[]
while True:
    inp=input("Enter items ")
    # quantity=int(input("Enter quantity "))
    x.append(inp)
    if inp!='0':
        quantity=int(input("Enter quantity "))
        q.append(quantity)
        s=s+menu.get(inp)*quantity 
    else:
        extra=int(input("Enter extra amount "))
        print(f"Your bill is {s+extra}")
        break
for i in range(len(x)):
    bill=(f"Item        Quantity        Amount\n{x[i]}       {q[i]}                 {menu.get(x[i])*q[i]}       ")
    i+=1
    break