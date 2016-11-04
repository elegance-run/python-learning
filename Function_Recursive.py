#递归求n！：

"""def function(n):
    if n==1:
        return 1
    else:
        return n*function(n-1)

n=int(input("输入一个自然数：\n"))
print(function(n))
"""

#递归出汉诺塔的移动步骤：
"""def Hanoi_move(n,a,b,c):
    if n==1:
        return print(a,"->",c)
    else:
        Hanoi_move(n-1,a,c,b)
        Hanoi_move(1,a,b,c)
        Hanoi_move(n-1,b,a,c)

Hanoi_move(5,'A','B','C')
"""

def greet(x= 'world'):
    print ('Hello,' +x, '.')
greet()
greet('Bart')
