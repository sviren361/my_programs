data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11,
     "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59,
      "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11,
       "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())
x=list(data.values())
ua=[]
a=[]
for item in x:
    if item<18:
        ua.append(item)
    else:
        a.append(item)
print(ua)
print(a)
income=(len(ua)*5)+(len(a)*20)
print(income)

ua2=[]
a2=[]
for item in x:
    if item<age:
        ua2.append(item)
    else:
        a2.append(item)
print(ua2)
print(a2)
income2=(len(ua2)*5)+(len(a2)*20)
print(income2)

growthrate=((income2-income)/income)*100
print(growthrate)