def transform(b):
    for i in range(len(b)-1):
        
        if b[i]=='1':
            b[i]='0'
            if b[i+1]=='0':
                b[i+1]='1'
            else:
                b[i+1]='0'
    return b
a=list('11111111111111111111')
c=a.copy()
print(a)

while a!=transform(c):
    a=transform(c)
print(a)