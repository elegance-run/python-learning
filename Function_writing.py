"""def my_abs(m):
    if m>0:
        return m
    elif m<0:
        return -m
    else:
        return 0

a=int(input("请输入一个实数：\n"))
print(my_abs(a))
"""

"""
def square_of_num(List):
    sum=0
    for x in List:
        sum=sum+x*x
    return sum

i=0
list=[]
n=int(input("请输入一个list的长度：\n"))
while i<=n-1:
    m = int(input("请输入一个整数：\n"))
    list.append(m)
    i=i+1

print(square_of_num(list))
"""

a=range(1,5)
b=range(1,4)
c=sum([x for x in b if x in b])
print(c)
