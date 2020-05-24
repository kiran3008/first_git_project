L = [10, 20, 30, 40, 50, 60]
L1 = [item ** 2 for item in L]
print(L1)

L = [5, 7, 2, 8, 6, 11, 13, 14]
L1 = [x for x in L if x % 2 == 0]
print(L1)

L = [[10, 20, 1, 2], [3, 4, 5, 6]]
L1 = []
for x in L:
    for y in x:
        L1.append(y)
print(L1)

L1 = [y for x in L for y in x]
print(L1)

L1 = [y for x in L for y in x if y % 2 == 0]
print(L1)

d = {'a': 10, 'b': 20, 'c': 30}
d1 = {}
for k in d:
    d1[k] = d[k] ** 2
    print(d1)

d1 = {key: d[key] ** 2 for key in d}
print(d1)
