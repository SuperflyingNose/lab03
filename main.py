n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
napr = int(input())
if(napr == 1):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
else:
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
print(a)