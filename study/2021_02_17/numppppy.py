import numpy as np

# a = np.array([1, 2, 3, 4], dtype='int32')
# b = np.array([4, 5, 6, 7], dtype='int64')
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)
#
# c = a + b
#
# print(c)
# print(c.dtype)


# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int32')
# b = np.array(range(1, 10))
# c = np.array(range(0, 10, 2), dtype='int64')
#
# print(a)
# print(b)
# print(c)


# a = np.array([[1, 1], [2, 2], [3, 3]])
#
# print(a)
# print(a.flatten())


# a = np.array([1, 2, 3])
# b = np.array([[4, 5, 6], [7, 8, 9]])
#
# print(np.append(a, b))
# print(np.append([a], b, axis=0))


# array3 = np.random.randint(10, size=(5, 3, 2))
# # print(array3)
# # print(np.sum(array3, axis=0))
# # print(np.sum(array3, axis=1))
# print(np.sum(array3, axis=2))


# a = np.array([23, 45, 67, 7, 2, 30, 34, 82])
# print(a)
#
# print(a.max())
# print(a.min())
# print(a.mean())
#
# print()
#
# b = np.array(np.random.randint(0, 100, size=10))
# print(b)
#
# print(b.max())
# print(b.min())
# print(b.mean())
#
# print(np.append(a, b))

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a@b)
# print(a**2)


# print(np.arange(0, 10))
# print(np.linspace(0, 10, 5))


# a1 = np.full((3, 3), 2)
# print(a1)
#
# a2 = np.arange(1, 13)
# print(a2)
#
# a3 = np.arange(3, 51, 3)
# print(a3)
#
# a4 = (np.linspace(0, 20, 5))
# print(a4)


# a1 = np.arange(1, 13)
# print(a1.reshape(2, 6))
#
# a2 = np.arange(1, 31)
# print(a2.reshape(3, 10))
#
# a3 = a2.reshape(6,5)
# print(a3)
#
# a4 = np.transpose(a3)
# print(a4)


# a = np.array([1, 3, 4])
# x = np.insert(a, 1, 2)
# print(x)
#
# a = np.array([[1, 1], [2, 2], [3, 3]])
# y = np.insert(a, 1, 4, axis=0)
# print(y)
#
# print(np.insert(a, 1, 4, axis=1))

# a = np.array(np.random.randint(1, 101, size=15))
# print(a.reshape(3, 5))


# a = np.arange(1, 11)
# print(a)
#
# print(a[np.array([1, 3, 5, 7])])
# print(a[np.array([0, 2, 4, 6, 8])])
#
# print(a[5:])
# print(a[6:])
# print(a[0:3])
# print(a[::2])
# print(a[::-2])
