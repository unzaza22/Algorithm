import random
import time

def mergeSort(arr,l,r):
    if l < r:
        m = (l+(r-1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


mergeSort_List = []

def mergeSort_Run():
    for Random in range(20000, 100001, +20000):
        total_List = []
        random_Sample = random.sample(range(1, Random + 1), Random)
        merge(random_Sample, 0, 2, len(random_Sample) - 1)
        # print("After Merge = ", random_Sample)

        for _ in range(10):
            random_Sample_Copy = random_Sample.copy()
            start_time = time.time()
            mergeSort(random_Sample_Copy, 0, len(random_Sample_Copy) - 1)
            end_time = time.time()

            total_time = end_time - start_time
            total_List.append(total_time)

        # print("time = ",total_time)
        # print("After mergeSort = ", random_Sample_Copy)
        mergeSort_List.append(min(total_List))
        # print("quick_List = ", mergeSort_List)



mergeSort_Run()
print("quick time = ", mergeSort_List)