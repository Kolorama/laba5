d = []
s = [1, 3, 5, 3, 5, 2, 6]
for x in s:
    if s.count(x) > 1:
        if x not in d:
            d.append(x)
print("zadanie 2")
print(d)