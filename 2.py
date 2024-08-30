a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(list(set(a)))

print(list(set(a)) + list(set(b)))

c = list()
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            
print(list(set(c)))
