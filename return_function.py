
#用返回函数方法定义求和函数：
'''def lazy_sum(*args):
    def sum():
        ax=0
        for x in args:
            ax=ax+x
        return ax
    return sum
f=lazy_sum(1,2,3,4)
#print(f)  #此时返回的是一个函数；
print(f())#函数调用时才可返回结果；
'''

#为何三个函数的返回值均为9；
'''def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs#返回函数引用了变量，此时函数并非立即执行，所有的函数都返回时，变量的值已经改变；
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
'''

#fixed:
def counter():
    fs=[]
    def p(j):
        def f():
            return j*j
        return f

    for x in range(1,4):
        fs.append(p(x))
    return fs

f4,f5,f6=counter()
print(f4())
print(f5())
print(f6())