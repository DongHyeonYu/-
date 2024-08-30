
def duplicate(a):
    return list(set(a))

def merge(a,b):
    return list(set(a+b))

def intersection(a,b):
    c = list()
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    return c


            
if __name__ =='__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(a)
    print(b)
    x = duplicate(a)
    y = merge(a,b)
    z = intersection(a,b)
    print(x)
    print(y)
    print(z)

# adfasdfasd
