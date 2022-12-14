import numpy as np

# 在numpy中，ndarray形式的数据，也是需要我们去做一定的基于统计学的分析的，
# 常见有min,max,median,mean,std,var

a=np.random.randint(50,100,[10,5])
print('a{}'.format(a))
# a[[81 87 63 72 93]
#  [63 94 67 94 79]
#  [90 81 53 97 75]
#  [80 70 72 68 86]
#  [99 67 57 77 53]
#  [78 54 76 72 86]
#  [89 65 92 93 56]
#  [62 74 65 99 56]
#  [72 93 93 88 85]
#  [54 74 78 58 51]]

# 在统计运算里，numpy中axis0代表列，1代表行，只是在这些api中
print('max{}'.format(np.max(a,1)))  # 每行最大值
print('min{}'.format(np.min(a,1)))  # 每行最小值
print('std{}'.format(np.std(a,1)))
print('mean{}'.format(np.mean(a,1)))
# max[93 94 97 86 99 86 93 99 93 78]
# min[63 63 53 68 53 54 56 56 72 51]
# std[10.6658333  13.03226765 15.10496607  6.76461381 16.4632925  10.6282642
#  15.42724862 15.06519167  7.73045924 10.91787525]
# mean[79.2 79.4 79.2 75.2 70.6 73.2 79.  71.2 86.2 63. ]

# 每列中值最高的是哪一行,返回对应行下标
print(np.argmax(a,0))
# [4 1 8 7 0]
# 每列中值最小的是哪一行，返回对应行下标
print(np.argmin(a,0))
# [9 5 2 9 9]






