#print(list(range(1,11)))

'''l=list(range(1,11))
print(l)

r=[]
for i in l:
    r.append(i*i)
print(r)
'''

'''l=['A','B','C']
j=['X','Y','Z']
r=[]
for i in l:
    for m in j:
        r.append(i+m)
print(r)

print(i+m for i in l for m in j)
'''


'''import os
for d in os.listdir('.'):
    print(d)
'''

L = ['Hello', 'World', 18, 'Apple', None]
l2=[s.lower() for s in L if isinstance(s,str)]
print(l2)
'''r=[]
for s in L:
    if isinstance(s,str)==True:
         r.append(s)
    else:
        continue
print(r)
'''