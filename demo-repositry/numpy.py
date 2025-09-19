import numpy as np
a=np.array([10,20,30])
print(a)
a=[10,20,30]
b=np.asarray(a,dtype=float)
print(b)
a=[[10,20],[30,40]]
b=np.asarray(a,order='C')
print(b)
for i in np.nditer(b):
 print(i)
a = b"welcome to vscode numpy"
arr_frombuffer = np.frombuffer(a, dtype='S1', count=20, offset=0)
print(arr_frombuffer)
a = [10, 20, 30, 40, 50]
arr_fromiter = np.fromiter(a, dtype=int)
print(arr_fromiter)
a=np.zeros(4)
print(a)
a=np.zeros([2,3])
print(a)
a=np.full([2,3],5)
print(a)
a=np.random.rand(2,3)
print(a)



