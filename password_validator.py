password = input("Enter password ")
ss = ["!", "@", "#", "$", "%", "&", "*"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0
num_count = 0
for i in password:
    if i in ss:
        count = count+1
    if i in num:
        num_count = num_count+1
if count >= 2 and num_count >= 2 and len(password) >= 7:
    print("Strong")
else:
    print("Weak")
