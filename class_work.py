from functools import reduce
import string

#第一题：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normolize(name):

    x=name[0].upper()
    y=name[1:].lower()

    return ("%s%s" %(x,y))

L1=['Adam','LISA','barT']
L2=list(map(normolize,L1))
print(L2)

#第二题：Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(List):
    return reduce(lambda x,y:x*y,List)  #python中lambda是一个表达式，可以返回一个结果；

L1=[1,2,3,4,5]
L2=prod(L1)
print(L2)


#第三题：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
#对整数部分进行操作：
def char_int(s):
    def fn(x, y):
        return 10 * x + y

    def char_int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char_int,s))


print(char_int('536274'))
#对小数部分操作：

