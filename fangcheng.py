#解一元二次方程a(x*x)+bx+c=0
#math.sqrt()计算平方根
import math
def quad(a,b,c):
    d = b*b-4*a*c
    if d < 0:
	    print('no')    #还需再处理
    else:
	    x1 = (-b+math.sqrt(d))/(2*a)
	    x2 = (-b-math.sqrt(d))/(2*a)
	    return(x1,x2)

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

f = quad(a,b,c)

print(f)

#在IDLE中代码运行正常，但似乎格式缩进有问题（line8），保存后无法正确执行，待查。
#恢复正常

#再次提交