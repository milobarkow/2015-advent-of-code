a = [1, 2, 3, 4]
print(a)
a.append(a.pop(a.index(a[0])))
print(a)
