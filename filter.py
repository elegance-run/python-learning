#用filter过滤掉不符合要求的序列：
'''def is_odd(n):
    return n%2==1
l=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(l)
'''


#将为空的元素删除：

'''def not_empty(s):
    return s and s.strip()
l=['  A',' ','B','I Love You...']
L=list(filter(not_empty,l))
print(L)
'''

#判断一个数是不是回数，并输出1:1000内所有的回数；
'''def is_palindrome(n):
    return n==int(str(n)[::-1])
s=range(1,1000)
output=filter(is_palindrome,s)
print(list(output))
'''

#筛选法找出素数：

def _odd_iter():#产生一个奇数序列；
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):#筛选函数：
    '''for x in range(2,n/2):
        if n%x==0:
            return False
        else:
            return True
    '''
    return lambda x:x%n>0


def primes():#生成器不断返回下一个符合要求的素数；
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

if __name__=='__main__':
    main()