def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]

list = [65, 64, 43, 23, 21, 12, 90]
bubble_sort(list)
print("sorted array is:", list)