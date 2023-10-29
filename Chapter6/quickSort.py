import random
import time

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


quickSort_List = []

def quickSort_Run():
    for Random in range(20000, 100001, +20000):
        total_List = []
        random_Sample = random.sample(range(1, Random + 1), Random)
        partition(random_Sample, 0, len(random_Sample) - 1)
        # print("After partition = ", random_Sample)

        for _ in range(10):
            random_Sample_Copy = random_Sample.copy()
            start_time = time.time()
            quickSort(random_Sample_Copy, 0, len(random_Sample_Copy) - 1)
            end_time = time.time()

            total_time = end_time - start_time
            total_List.append(total_time)

        # print("After quickSort = ", random_Sample_Copy)
        quickSort_List.append(min(total_List))
        # print("quick_List = ", quickSort_List)



quickSort_Run()
print("quick time = ", quickSort_List)