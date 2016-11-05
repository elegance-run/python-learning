#计算100以内所有奇数的和：
"""
n=1;
sum=0;
while True:
    sum=sum+n;
    n=n+2;
    if n>=100:
        break;
print(sum);
"""


#计算1+2+4+8+16+...前20项的和：

sum=0;
n=1;
m=1;
while True:
    sum=sum+n;
    n=2*n;
    m=m+1;
    if m>20:
        break;
print(sum);