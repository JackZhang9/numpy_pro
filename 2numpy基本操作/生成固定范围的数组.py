# 导入numpy
import numpy as np

# 一.生成固定范围的数组，如：等步长

# 1.创建指定数量的等差数组
# np.linspace(start,stop,num,endpoint,dtype)
c=np.linspace(3,101,num=50,dtype=np.int32)  # 起始值3，终止值101，元素数量50个
print(c,c.size,c.dtype)  # 现学现用，前面知道ndarray有属性szie，表示元素个数，这里直接使用size查看元素个数，
# [  3   5   7   9  11  13  15  17  19  21  23  25  27  29  31  33  35  37
#   39  41  43  45  47  49  51  53  55  57  59  61  63  65  67  69  71  73
#   75  77  79  81  83  85  87  89  91  93  95  97  99 101] 50 int32

# 2.创建指定步长的等差数组
# np.arange(start,stop,step,dtype)
c2=np.arange(3,101,2)  # 起始值3，终止值101，步长为2，和上面的ndarray类似的效果，但是arange()前包后不包，所以101没算里面
print(c2,c2.size,c2.dtype)
# [ 3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
#  51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97
#  99] 49 int32

# 3.创建指定数量的等比数组
# np.logspace(start,stop,num)
c3=np.logspace(0,3,4,dtype=np.int32)  # 生成4个数[0,1,2,3]10的0次方1,1次方10,2次方100,3次方1000
print(c3,c3.size,c3.dtype)     # 感觉不怎么好用
# [   1   10  100 1000] 4 int32