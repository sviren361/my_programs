players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean=0
for i in players:
    mean=mean+i
m=int((mean/len(players)))
var=[]
for i in players:
    var.append((i-m)**2)
print(var)
v=0
for j in var:
    v=v+j
vm=(v/len(var))
f=int(vm**0.5)
k=0
for i in players:
    if i in range(m-f,m+f):
        k+=1
print(k)