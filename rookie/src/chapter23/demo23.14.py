# NumPy常用函数：计算中位数和方差
from numpy import *
a = array([4,2,1,5])
print(median(a))
a = array([4,2,1])
print(median(a))

price =loadtxt('data.csv', delimiter=',', usecols=(6,),unpack=True)
print(price)
print(median(price))

print('方差：',var(price))

print("float number:{pi:10.2f}".format(pi= pi))

