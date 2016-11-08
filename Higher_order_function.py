#高阶函数：

def fun(a,b,f):
    return f(a)+f(b)

m=int(input('输入一个数m：'))
n=int(input('输入一个数n：'))
l=fun(m,n,abs)
print(l)