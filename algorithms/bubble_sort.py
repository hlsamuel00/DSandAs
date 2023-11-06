def bubble_sort(array: list[int]) -> None:
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


from random import randint
bubble_array = [randint(1,100) for _ in range(10)]
print(bubble_array)

bubble_sort(bubble_array)
print(bubble_array)