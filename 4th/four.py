import numpy as np

#Задание 1
arr = np.arange(10)
print(
    "Average of %s EQ %-.7g" %
    (arr, np.mean(arr))
)
print()

#Задание 2
arr = np.random.randint(1, 21, size=10)
print(
    "Max int in %s: %d" %
    (arr, np.amax(arr))
)
print()

#Задание 3
print(
    "Min int in %s: %d" %
    (arr, np.amin(arr))
)
print()

#Задание 4
print(
    "Index of max(\n\t%s\n) = %d: %d" %
    (arr, np.amax(arr), np.argmax(arr))
)
print()

#Задагие 5
print(
    "Index of min(\n\t%s\n) = %d: %d" %
    (arr, np.amin(arr), np.argmin(arr))
)
print()

#Задагие 6
arr = np.random.randint(-20, 21, size=10) #[-20; 21)
print(
    "Replacing negative numbers with 0:\n\tSource: %s\n\tResult: %s" %
    (arr, np.maximum(arr, 0))
)
print()

#Задагие 7
print(
    "Replacing positive numbers with 0:\n\tSource: %s\n\tResult: %s" %
    (arr, np.minimum(arr, 0))
)
print()

#Задагие 8
arr = np.random.randint(1, 7, size=5)
print(
    "Cube all array values:\n\tSource: %s\n\tResult: %s" %
    (arr, np.power(arr, 3))
)
print()

#Задагие 9
print(
    "Sqrt of all array values:\n\tSource: %s\n\tResult: %s" %
    (arr, np.sqrt(arr))
)

#Задание 10
print(
    "Sum of all array values: %d" %
    np.sum(arr)
)