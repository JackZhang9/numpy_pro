# 这一节介绍numpy唯一数据类型，ndarray,如何创建，及其属性，形状，类型
# 先导入numpy，后续默认导入numpy
import numpy as np

# 一.numpy创建一个ndarray有多种方法，

# 方法1.直接用array创建,array可以直接生成多维数组
a1=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])  # 创建一个包含两个二维矩阵的三维张量
print(a1,type(a1))
# 一个小tips，用括号看ndarray维度，3个括号，三维张量，
# [[[1 2 3]
#   [4 5 6]
#   [7 8 9]]
#
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]] <class 'numpy.ndarray'>

# 方法2.使用arange创建,只能生成一维向量,第一位是起始位，第二位是终止位，第三位是步长，
a2=np.arange(2,10,2)
print(a2,type(a2))
# [2 4 6 8] <class 'numpy.ndarray'>


# 二.numpy的ndarray的属性

# ndarray反映了数组本身自带的信息,所以查看属性时不要带()，因为它不是函数，而是一种天生信息，shape,ndim,size,itemsize,dtype
print(a1.shape)   # 查看ndarray形状
print(a1.ndim)  # 查看维度
print(a1.size)  # 查看元素个数
print(a1.itemsize)  # 查看一个元素的字节长度
print(a1.dtype)  # 查看元素类型
# (2, 3, 3)
# 3
# 18
# 4
# int32


# 三.numpy的ndarray的形状

# ndarray本质是一些标量，向量，矩阵，张量，而这些数据都是可以改变形状的(不改变元素)
# 零维标量，一维向量，二维矩阵，三维张量，但它们的数据类型都是ndarray
print(a1.shape)   # 查看a1形状，三维张量,就是多个矩阵的叠加
print(a2.shape)  # 查看a2形状，一维向量
print(np.array([[1,2,3],[4,5,6]]).shape)  # 二维矩阵
print(np.array(3).shape)  # 零维标量
# (2, 3, 3)
# (4,)
# (2, 3)
# ()


# 四.numpy中元素的类型

# numpy中元素类型为dtype,dtype有多种类型，可以通过dtype在创建ndarray时指定
# 常用np.float32,np.string,
a3=np.array([[1,2,3],[7,5,9]],dtype=np.float32)
print(a3.dtype)  # 通过dtype查看ndarray中元素类型


# 在numpy中，ndarray有多种属性，其中shape是最重要的属性，dtype是ndarray中元素的类型，查看属性的方法都直接 ndarray.属性














