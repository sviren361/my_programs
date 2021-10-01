def is_p(number) -> bool:
    number = abs(number)
    return round(number**(1/3))**3 == number


def closest(cubes, k):
    return cubes[min(range(len(cubes)), key=lambda i: abs(cubes[i]-k))]


n = int(input())
cubes = []
for i in range(1, 100):
    x = i*i*i
    cubes.append(x)
lst = []
d = input().split()
sum = 0
for i in d:
    sum += int(i)
cube = is_p(sum)
if cube:
    print("Yes")
else:
    k = sum
    sol = (closest(cubes, k))
print(sum-sol)
