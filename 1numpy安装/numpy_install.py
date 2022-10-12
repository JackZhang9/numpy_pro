# 安装指令
# pip install numpy -i http://pypi.tuna.tsinghua.edu.cn.simple

# 测试安装是否成功

import numpy as np
# 自定义一个数组
a=np.array([1,2,3])
print(a,type(a))

# 初始化一个1到2的数组,arrange()传入一个整数，返回一个ndarray
b=np.arange(3)
print(b,type(b))

# 可以看到numpy安装成功，对应数据类型也全是ndarry
# [1 2 3] <class 'numpy.ndarray'>
# [0 1 2] <class 'numpy.ndarray'>

# 小结：在numpy中，数据类型只有一种，N_dimensional