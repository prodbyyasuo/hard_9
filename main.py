file = open('9.txt')
cnt = 0

for f in file:
    a = [int(x) for x in f.split()]
    povt = [x for x in a if a.count(x) > 1]
    nepovt = [x for x in a if a.count(x) == 1]
    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 != 0]
    if len(nepovt) in [3, 4]:
        sr_nepovt = sum(nepovt) / len(nepovt)
        sr_povt = sum(povt) / len(povt)
        if sr_nepovt < sr_povt:
            if sum(a) > 2500:
                if len(even) >= 1 and len(even) > len(odd):
                    cnt += 1

print(cnt)