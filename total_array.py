import array as ar
a=ar.array('i',[5,6,8])
sum=0
for i in range(len(a)):
    sum=sum+a[i]
for i in range (0, 3):
        print (a[i],end='')
print()
    
print(sum)

