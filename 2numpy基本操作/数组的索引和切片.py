import numpy as np


# 在numpy中，ndarray的内容可以通过索引或切片来访问或修改，这和python里的list数据类型一样，可以理解为进阶版的list,
# 事实上，ndarray确实源于list，为了解决list不能解决的问题而产生

# 一维向量，二维矩阵，三维张量，都可以用同一套方法索引：[:,:]。前面是行数，后面是列数，这是二维。如果是三维，[:,:,:],第一个表示矩阵的第几个，第二个表示矩阵行，第三个是矩阵第几列
# 同理，四维[:,:,:,:],第一个是第几个张量，第二个是张量中第几个矩阵，第三个是矩阵中第几行，第四个是矩阵中第几列。
# 注意：索引也是前包后不包的。

# 创建一个ndarray数组
a2=np.random.normal(1,2,[2,3])   # 创建一个两行三列的高斯分布ndarray，二维矩阵
print(a2)
print(a2[0,2])  # 通过0~n的下标进行索引
print(a2[0,1:3])  # 0表示第0行，1:3表示第1到2列
# [[ 2.56605579 -0.6351259   1.2397155 ]
#  [-3.30491626  2.26000669 -0.71338566]]
# 1.239715495774618
# [-0.6351259  1.2397155]

a3=np.random.normal(1,2,[2,2,3])  # 得到三维张量
print(a3)
print(a3[0,0,1])  # 第0个矩阵，第0行，第1列
# [[[-1.40160486  0.09116682  2.28538562]
#   [-1.70098611  1.52412843  3.68857685]]
#
#  [[ 1.84104473  2.39073006  0.22750329]
#   [ 1.31107614  1.26438062  3.35833742]]]
# 0.09116681512876612

# 尊重一个原则，[]，先张量个数，再矩阵个数，再行数，再列数，
# 索引为负数，-1为“最后”，来看看
a4=np.random.normal(1,5,[4,3])
print('a4{}'.format(a4))
# 二维矩阵
print('a4最后一行{}'.format(a4[-1]))  # 最后一行
print('a4行逆序{}'.format(a4[::-1]))  # 行逆序,对比最大单元小一单元的逆序，矩阵中就是向量，张量里就是矩阵


# 小tips，对数组进行[::-1]即可逆序，对于哪一维逆序就对哪一维[::-1]
b=range(12)
print([i for i in b][::-1])
b2=np.random.normal(1,5,[2,3,2])  # 对每个矩阵逆序，矩阵中每一行逆序，每一列逆序
print('b2{}'.format(b2))
print('b2逆序{}'.format(b2[::-1,::-1,::-1]))
















