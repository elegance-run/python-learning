#求一元二次方程的解：
import math

def Solution(a,b,c):
    temp=b*b-4*a*c
    if a==0:
        return (-b/c)
    elif temp<0:
        return("无解；")
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1,x2

a=float(input("输入二次项系数a：\n"))
b=float(input("输入一次项系数b：\n"))
c=float(input("输入常数项系数c：\n"))
print(Solution(a,b,c))
