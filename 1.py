a = input()
p = print
if a[0]=='-':
    b = list(a)[1:]
else:
    b = list(a)
cnt =0
for i in range(1,len(b)):
    if i%3==0:
        b.insert(-(i+cnt),',')
        cnt+=1
if a[0]=='-':
    p(f"-{''.join(b)}")
else:
    p(''.join(b))