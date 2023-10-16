def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current element is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the minimum element with the current element

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
####
list = [4,44,54,567,33]
min_list = max(list)
print(min_list)
index = list.index(min_list)
