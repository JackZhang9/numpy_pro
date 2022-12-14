import numpy as np


# 不知不觉到了numpy教程的最后一章，通过前面的学习，现在对于numpy有一个大致的了解，
# 在numpy中，我们处理的对象是ndarray，多维数组，可以是一个零维标量，一维向量，二维矩阵，三维张量，四维张量，


# 1.二维矩阵

# 矩阵加法，行列数相同的矩阵对应值可以直接相加，
# 矩阵乘法，一个数乘以矩阵，和矩阵中每个数相乘
# 矩阵乘法规则，前一个矩阵的列数，等于后一个矩阵的行数，(和向量也是一样，可以理解向量是一个列矩阵或行矩阵)
# mxn矩阵*nxo矩阵=mxo矩阵，向量叉乘

a=np.arange(1,10).reshape([3,3])
b=np.arange(1,10).reshape([3,3])
multiplyab=np.multiply(a,b)   # 这种乘法是点乘，即对应位置元素的乘积，叫哈达玛积
ab=a*b                        # 也是点乘，对应位置元素的乘积
print('a\n{}\nb\n{}\nab\n{}\nab{}\n'.format(a,b,multiplyab,ab))
# a
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# b
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# ab
# [[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]
# ab[[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]

# 矩阵叉乘
matmulab=np.matmul(a,b)  # 建议使用这个，可读性强，矩阵乘法，而且是np里的函数，矩阵乘矩阵
matsignal=a @ b
matdot=np.dot(a,2)   # 少用，容易有歧义，矩阵乘标量
print('{}\n{}\n矩阵乘\n{}'.format(matsignal,matdot,matmulab))
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]
# 矩阵乘
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]















