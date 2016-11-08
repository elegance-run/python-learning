#map（）的用法：
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''def fun(x):
    return x*x

r=map(fun,[1,2,3,4,5])
p=map(str,[1,2,3,4,5])
print(list(r))
print(list(p))
'''


#reduce的用法：

from functools import reduce
'''def fn(x,y):
    return 10*x+y

l=[1,2,3,4,5,6]
print(reduce(fn,l))
'''


#将输入的一个字符串转化成整数；
def str_int(s):
    def fn(x, y):
        return 10 * x + y

    def char_int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char_int,s))

s='1267847874'
print(str_int(s))
