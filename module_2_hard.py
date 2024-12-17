n = int(input("Введите число для подбора пароля: "))
b = []
for i in range(1, n):
    for j in range(n, 1, -1):
        j -= 1
        if i + j <= 2:
            continue
        if n % (i + j) == 0:
            if i < j:
                a = [i, j]
                b.append(a)
b.sort()
#print(b)
list_my = []
for i in b:
    for k in i:
        list_my.append(k)
print (*list_my)