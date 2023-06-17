import numpy as np

#Задание 1
arr = np.arange(10)
print(arr)
print()

#Задание 2
arr = np.ones((3, 3))
print(arr)
print()

#Задание 3
arr = np.random.randint(1, 11, size=(2, 2))
print(arr)
print()

#Задание 4
arr = np.random.rand(5, 5)
print(arr)
print("Average: %.10g" % np.mean(arr))
print()

#Задагие 5
arr = np.random.rand(5, 5)
print(arr)
print("Cols sums: ", arr.sum(axis=0))