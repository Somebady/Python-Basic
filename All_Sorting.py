
# Selection Sort
# Get the minimum value and place in 0th Index then repeat it again


list1 = [1, 4, 6, 33, 22, 65, 45, 34, 45, 55, 687, 12, 32, 19, 20, 33, 231, 31]
# # Selection sort


def bubbleSort(list1):
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]


bubbleSort(list1)
print(list1)


# Bubble Sort
# comparing adjsent values and arrage them in order

def SelectionSort(list1):
    for i in range(len(list1)-1, 0, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]


SelectionSort(list1)
print(list1)


# Important Quick Sort
# list1 = [10, 15, 2, 7, 4, 5, 9, 0]


def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quickSort(list1, first, last):
    if first <= last:
        p = pivot_place(list1, first, last)
        quickSort(list1, first, p-1)
        quickSort(list1, p+1, last)


quickSort(list1, 0, len(list1)-1)
print(list1)

# Optimizing Quick Sort
# list1 = [10, 15, 2, 7, 4, 5, 9, 0]


def pivot_place(list1, first, last):
    low = list1[first]
    mid = list1[(first+last)//2]
    high = list1[last]
    pivot = sorted([low, mid, high])[1]  # get the median of 3
    pvt_idx = list1.index(pivot)  # Get selected pvt_index
    # Swap pvt to first & now first act as pivot
    list1[pvt_idx], list1[first] = list1[first], list1[pvt_idx]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right-1
        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quickSort(list1, first, last):
    if first <= last:
        p = pivot_place(list1, first, last)
        quickSort(list1, first, p-1)
        quickSort(list1, p+1, last)


# quickSort(list1, 0, len(list1)-1)
# print(list1)


# Complexity Of Quick SOrt
# Worst Case--O(n*2), #Avg Case and Best case (nlogn)
# Worst case is array is already in sorted order or reversed sorted
# Quick Sort works best for long list & Insertion sort work best for short lists

# Hybrid Quick Sort
# # Using Insertion sort for smaller Partition & Quick for larget partition, Provide us the best complexity


# Merge Sort

list1 = [1, 4, 6, 33, 22, 65, 45, 34, 45, 55, 687, 12, 32, 19, 20, 33, 231, 31]


def mergeSort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
            else:
                list1[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


# mergeSort(list1)
# print(list1)

# MErge Sort
# nlog(n) is the complexity in every case, Sorting linked list with merge sort is the best way to sort linkedlist


# Insertion Sort

list1 = [1, 4, 6, 33, 22, 65, 45, 34, 45, 55, 687, 12, 32, 19, 20, 33, 231, 31]


def insertionSort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        pos = i
        while pos > 0 and key < list1[pos-1]:
            list1[pos] = list1[pos-1]
            pos -= 1
        list1[pos] = key


insertionSort(list1)
print(list1)

# Insertion Sort is best for small set of values

# Binary Search Implementation


list1 = [1, 4, 6, 33, 22, 65, 45, 34, 45, 55, 687, 12, 32, 19, 20, 33, 231, 31]
mergeSort(list1)  # Binary Search required sorted array

print(list1)

# Recursive Way


def Bns(list1, val, first=0, last=len(list1)-1):
    mid = (first+last)//2
    if list1[mid] == val:
        print(f'Found @idx. {mid}')
        return 0
    if last > first:
        if val > list1[mid]:
            Bns(list1, val, mid+1, last)
        else:
            Bns(list1, val, first, mid)
    else:
        print('Not FOund')
        return 0


Bns(list1, 1)

# Iterative Way


def BnsIt(list1, val, first=0, last=len(list1)-1):

    while last >= first:
        mid = (first+last)//2
        if list1[mid] == val:
            print(f'Found @idx. {mid}')
            return 0
        if list1[mid] > val:
            last = mid-1
        else:
            first = mid+1
        print(last, first)
    print("Key Not Found")
    return 0


BnsIt(list1, 8)

# Time Complexity of Binary Search is log(n) in both
# Space complexity in recursive is went to log(n) and in iterative case O(1)
