d = {'a': 1, 'b': 2, 'c': 3}

'''for key in d:
    print(key,':',d.get(key))
'''

'''for key,value in d.items():
    print('%s:%s'%(key,value))
'''

'''from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
'''


from collections import Iterable
'''l=['Russel Westbrook','Derik Rose','Leonard','Chris Paul']
for i,value in enumerate(l):
    print(i,value)
'''


'''d=[(1,1),(2,3),(4,5)]
for x,y in d:
    print(x,y)
'''

n=1
m=10
dict={}
while n<=10:
    dict[n]=m
    n=n+1
    m=m-1
for k,v in dict.items():
        print(k,v)