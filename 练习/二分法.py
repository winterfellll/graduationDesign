def binarySearch(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if x == arr[mid]:
            return mid + 1
        elif x > arr[mid]:
            low = mid
        else:
            high = mid


array = [3, 5, 9, 13, 55, 98, 106, 139]
target = 13
print(f'查找值是第{binarySearch(array, target)}个')
