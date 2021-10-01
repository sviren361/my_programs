def Code_Year(year):
    if year in range(1600, 1699):
        return 6
    elif year in range(1700, 1799):
        return 4
    elif year in range(1800, 1899):
        return 2
    elif year in range(1900, 1999):
        return 0
    elif year in range(2000, 2099):
        return 6


date = input("Enter date(DD) ")
month = input("Enter month(fisrt 3 letters) ").upper()
year = input("Enter year(YYYY) ")

Code_Day = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]

Code_Month = {"JAN": 0, "FEB": 3, "MAR": 3, "APR": 6, "MAY": 1,
              "JUN": 4, "JUL": 6, "AUG": 1, "SEP": 5, "OCT": 0, "NOV": 3, "DEC": 5}

y = (int(year[2:4]))//4
c_m = (Code_Month.get(month))
c_y = Code_Year(int(year))

if int(year[2:4]) % 4 == 0:
    access = ((int(year[2:4])+y+int(date)+c_m+c_y) % 7)-1
else:
    access = (int(year[2:4])+y+int(date)+c_m+c_y) % 7

print(f"The day of the date {date}/{month}/{year} is {Code_Day[access]}")
