start=2
end=int(input("Enter a no. for range from 1 to "))
l=[]
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        l.append(i)
print(f"There are {len(l)} prime no.s from 1 to {end} which are")
print(l)