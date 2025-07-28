def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        # Swap backwards until the correct place is found
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Example:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
