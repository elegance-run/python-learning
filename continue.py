#只计算及格分数的平均分；
"""
score=[10,30,98,78,88,67,79,94,42];
sum=0;
n=0;
m=0;
print('及格的分数：');
for Score in score:
    if Score<60:
        continue;
    print(Score);
    sum=sum+Score;
    n=n+1;
print('平均分为：',sum/n);
"""



#通过continue语句计算100以内奇数的和；
sum=0
x=0
while True:
    x=x+1
    if x>100:
        break
    if x%2==1:
        sum=sum+x
        continue
print(sum)