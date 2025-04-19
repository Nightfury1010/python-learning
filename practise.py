import numpy as np

b = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
print(b)


a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.full_like(a, 100))

#all zeros matrix
a = np.zeros((3, 4))
print(a)

#all ones matrix
a = np.ones((3, 4))
print(a)

#all 1s matrix
n = np.ones((3,2,2))
print(n)

#any other number matrix
a = np.full((3, 4), 5, dtype=float)
print(a)

 #random matrix
a = np.random.rand(3, 4)
print(a)

#random integer matrix
a = np.random.randint(10, size=(3, 4))
print(a)

i=np.ones((5,5))
j=np.zeros((3,3))
j[1,1]=9
i[1:-1, 1:-1] = j
print(i)


output = np.zeros((7,7))
z = np.ones((5, 5))
z[1, 1] = 5
output[1:-1, 1:-1] = z
print(output)


a = np.array([1, 2, 3, 4, 5])
b = a
b[2] = 20
print(b)  # a is also changed because b is a reference to a

c = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
d = np.max(c, axis=1).sum()
print(d)  # 5 because a is a 1D array, axis=1 is not valid for 1D arrays


a = np.ones((2, 4))
b = a.reshape((4, 2))
print(b)

a = np.ones((2, 4))
b = a.reshape((2, 4))
print(b)


a = np.ones((2, 4))
b = a.reshape((8, 1))
print(b)