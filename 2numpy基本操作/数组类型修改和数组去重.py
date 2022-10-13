import numpy as np


# 1.在numpy中，修改ndarray中元素数据类型
a=np.random.normal(1,3,[2,3])

print(a.dtype)
# float64

# 修改类型
a1=a.astype(np.int32)   # 修改成int32
print(a1.dtype)
# int32
a2=a.tobytes()  # python字节
print('tobytes{}'.format(a2))
# tobytesb'\x18`\xea\xd6\x19\x8a\x1f\xc0\xd3\xc7`\xcaA,\x01@H\xa1\xdc\x18Z\xea\xbf?H(\xca\xf7\xbf{\xfb?\xb9\x03p\xbe\x91\xa7\x17@\xd5[0\xe8/\xe0\n@'


# 2.在numpy中，数组去重
b=np.array([[1,8,3,4],[2,9,4,5],[4,5,6,7],[6,7,4,1]])
print('b{},bshape{}'.format(b,b.shape))
# b[[1 2 3 4]
#  [2 3 4 5]
#  [4 5 6 7]
#  [6 7 4 1]],bshape(4, 4)
# 使用去重np.unique()
b2=np.unique(b)  # 去重后得到一个一维向量，很合理，因为这是去除了数组的排列规律的，新的规律就以向量升序排列
print('b2{},b2shape{}'.format(b2,b2.shape))
# b2[1 2 3 4 5 6 7 8 9],b2shape(9,)


















