def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) -1)
    
	
	
	
	
def binarySearchHelper(array, target, left, right):
    mid = (left + right) // 2
    while left <= right:
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binarySearchHelper(array, target, mid + 1, right)
        elif array[mid] > target:
            return binarySearchHelper(array, target, left, mid - 1)
    return -1
