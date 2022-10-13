import numpy as np

# 上一节学习了numpy的基本操作，都是对ndarray内部数据的操作，ndarray与外部如何发生关系，是这一节学习的内容，
# 首先讲，
# 1.逻辑运算，

a=np.random.randint(50,100,[10,5])   # 符合均匀分布的一个数组，10行5列
print('a{},ashape{}'.format(a,a.shape))

b1=a[6:]
print('b1{}'.format(b1))

b2=b1>60   # 在 numpy中，数组直接和数值比较，就能得到数组的逻辑值，在python中list不支持这样比较
print('逻辑{}'.format(b2))

b1[b1>60]=1     # 在b1中，大于60的变为1，将满足条件的设置为指定的值，
print('b3{}'.format(b1))


# 2.通用判断函数
# 用来判断一个整体的
# np.all()  这个函数只给出一个返回值，全部满足ture,一个不满足false，理解为串联，一票否决
c1=a[:2]
print(c1,np.all(c1>60))    #全部数大于60吗？不是

# np.any()  这个函数给一个返回值，满足一个就ture，一票通过制
print(c1,np.any(c1>80))  #有一个数大于80吗？有

# np.where(三元运算符)
# 以上例举例
# 在上例子中，b1[b1>60]=1，而小于60的数没有改变，此时可以改变
d=np.where(c1>60,1,0)  # 三元运算符，大于60,1。小于60为0。
print('c1{},d{}'.format(c1,d))

# 复杂一点，逻辑与
d1=np.where(np.logical_and(c1>60,c1<80),1,0)
print('d1{}'.format(d1))
# 逻辑或np.logical_or(x,y) 和逻辑与一样使用

# 列表生成式
ee=[i for i in range(10) if i>3]
print(ee)



