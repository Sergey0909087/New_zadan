# Задача 1
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i % 2 == 1:
        a.remove(i)
print(a)

for i in range(len(a)):
    a[i] = a[i] // 2
print(a)

# for i in a:
#     if i % 2 == 0:
#         print("Число четное", i, ': 2 = ', i / 2)