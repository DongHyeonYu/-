a = input()
if a.startswith('-'):
    b = list(a)[1:len(a)]
else:
    b = list(a)
cnt =0
for i in range(1,len(b)):
    if i%3==0:
        b.insert(-(i+cnt),',')
        cnt+=1
if a.startswith('-'):
    print(f"-{''.join(b)}")
else:
    print(''.join(b))
