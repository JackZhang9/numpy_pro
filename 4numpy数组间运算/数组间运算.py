import numpy as np

# 本节介绍numpy中使用到最多的数组之间的运算，详细介绍数组之间运算的特性

# 1.算术函数，就是加减乘除
a=np.random.randint(10,50,[4,4])
b=np.random.randint(12,60,[4,4])
# '+-*/'与使用np.add(x,y),np.subtract(x,y),np.multiply(x,y),np.divide(x,y)
print(a+b,a-b,a*b,a/b)
print(np.add(a,b),np.subtract(a,b),np.multiply(a,b),np.divide(a,b))


# 2.数学函数
# 在numpy中，提供了一些数学函数，标准三角函数，np.sin(),np.cos(),np.tan(),
# 指定四舍五入函数,np.around()保留几位小数,np.floor()向下取整，np.ceil()向上取整
a1=np.sin(a)
a2=np.cos(a)  # 下舍整数
a3=np.tan(a)  # 上入整数
print('a1{}a2{}a3{}'.format(np.around(a1,3),np.floor(a2),np.ceil(a3)))


# 3.聚合函数:对一组值执行计算并返回单一的值，
# 在前面已经接触过一些统计函数，如np.max(),np.min(),np.std(),np.mean(),np.var(),np.argmax(),np.argmin(),np.median()
# 再增加一些，
c=np.arange(1,16)
c=np.power(c,2)
print('sum={}'.format(np.sum(c)))  # 求和
print('prod={}'.format(np.prod(c)))  # 元素相乘
print('sqrt={}'.format(np.sqrt(c)))  # 开平方
print('power={}'.format(np.power(c,2)))  # 平方
print('exp={}'.format(np.exp(c)))  # 以e为底的指数函数
print('log={}'.format(np.log(c)))
# sum=1240
# prod=-297795584
# sqrt=[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
# power=[    1    16    81   256   625  1296  2401  4096  6561 10000 14641 20736
#  28561 38416 50625]
# exp=[2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06
#  7.20048993e+10 4.31123155e+15 1.90734657e+21 6.23514908e+27
#  1.50609731e+35 2.68811714e+43 3.54513118e+52 3.45466066e+62
#  2.48752493e+73 1.32348326e+85 5.20305514e+97]
# log=[0.         1.38629436 2.19722458 2.77258872 3.21887582 3.58351894
#  3.8918203  4.15888308 4.39444915 4.60517019 4.79579055 4.9698133
#  5.12989871 5.27811466 5.4161004 ]


# 4.数组与数的运算
# 就是每个元素加上数值，除以数值
d=np.random.normal(5,22,[2,6])
d1=d+1
d2=d/2
print('d{} d1{} d2{}'.format(d,d1,d2))


# 5.数组与数组的运算
# 数组与数组运算时，因为shape的不一样，所以需要补齐。广播机制
e1=np.random.normal(1,22,[4,1])
e2=np.random.normal(1,5,[3])
print('e1{}\ne2{}'.format(e1,e2))
e3=e1+e2   # 取两者最大值，行4，列3，广播机制，对两个数组都进行扩展，使两个数组都变成4行3列，
print('e3{}'.format(e3))   #
# e1[[-23.1788338 ]
#  [ -2.44418894]
#  [ -5.65600744]
#  [-23.32849452]]
# e2[ -6.58567783  -2.3162987  -11.13740831]
# e3[[-29.76451163 -25.4951325  -34.31624211]
#  [ -9.02986677  -4.76048763 -13.58159724]
#  [-12.24168528  -7.97230614 -16.79341575]
#  [-29.91417235 -25.64479321 -34.46590282]]


# 6.数组的拼接
# 前面一小节学习过数组的分割，有说到hsplit()水平分割，vsplit()垂直分割
# 对应的有水平分割就有水平组合，以及垂直组合，

# 1.水平组合
# np.hstack()
# 注意，hstack()里面输入一个元组()，要求行数相同，
m1=np.random.randint(5,60,[2,4])
n1=np.random.randint(20,80,[2,3])
mn=np.hstack((m1,n1))
print('m1={}\nn1={}\nmn={}'.format(m1,n1,mn))
# m1=[[33 28 45 49]
#  [23  9 36 26]]
# n1=[[46 44 77]
#  [73 36 78]]
# mn=[[33 28 45 49 46 44 77]
#  [23  9 36 26 73 36 78]]

# 2.垂直组合
# np.vstack()
# 注意，列数要相同
m2=np.random.randint(40,100,[2,7])
n2=np.random.randint(50,120,[3,7])
mn2=np.vstack((m2,n2))
print('m2={}\nn2={}\nmn2={}'.format(m2,n2,mn2))
# m2=[[98 80 49 77 69 55 70]
#     [89 64 44 96 56 82 74]]
# n2=[[ 68 113  59 105  73  52  52]
#     [ 80  50 102 107  89 102  73]
#     [ 88  78  69  85  94 118  69]]
# mn2=[[ 98  80  49  77  69  55  70]
#      [ 89  64  44  96  56  82  74]
#      [ 68 113  59 105  73  52  52]
#      [ 80  50 102 107  89 102  73]
#      [ 88  78  69  85  94 118  69]]


# 3. concatenate
# np.concatenate()
# 即可以按行拼接，又可以按列拼接，相当于一个函数实现了两个函数的功能
# 3.1水平组合，完成和np.hstack()相同的效果
con1=np.concatenate((m1,n1),1)  # axis设为1，水平组合
print('水平组合{}'.format(con1))

# 3.2垂直组合，完成和np.vstack()相同的效果
con2=np.concatenate((m2,n2))  # 默认为0，垂直组合，不用设置
print('垂直组合{}'.format((con2)))


# 5. 三维数组拼接
# 生成两个三维数组
m3=np.random.randint(3,50,[2,2,3])
n3=np.random.randint(60,100,[2,2,3])
# 建议就记忆一个concatenate()然后记得1是水平组合，0是垂直组合，
# 水平组合，张量中的垂直组合
con31=np.concatenate((m3,n3),1)
# 垂直组合，
con32=np.concatenate((m3,n3))
# axis2组合,这是一个水平方向上两个张量的拼接，张量中水平组合
con33=np.concatenate((m3,n3),2)
print('m3=\n{}\nn3=\n{}\ncon31=\n{}\ncon32=\n{}\ncon33=\n{}'.format(m3,n3,con31,con32,con33))










