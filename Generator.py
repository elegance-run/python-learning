#使用Generator打印出Fibonacci数列：
'''def Fibonacci(max):
    n=0
    a=0
    b=1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=Fibonacci(10)
while True:
    try:
        x=next(f)
        print('f:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
'''


def triangles():
    L=[1]

    while True:
        yield L
        L.append(0)
        L=[L[t-1]+L[t] for t in range(len(L))]
n=int(input('Please enter a number:'))
m=0
for t in triangles():
    print(t)
    m=m+1
    if m==n:
        break
