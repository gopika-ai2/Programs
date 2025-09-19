# defining the binary search recursive function to search for an element

def bs_recursive(arr, start, end, target):

# Base case: If the element is not present

if end < start:

return -1 

mid = (end + start) // 2 

# If the element is present at the middle

if arr[mid] == target:

return mid

# If the element at mid is greater than the target

elif arr[mid] > target:

return bs_recursive(arr, start, mid - 1, target)

else:

return bs_recursive(arr, mid + 1, end, target) 

def bs_iterative(arr, target):

start, end = 0, len(arr) - 1

 

while start <= end:

mid = (start + end) // 2 

if arr[mid] == target:

return mid

elif arr[mid] > target:

end = mid - 1

else:

start = mid + 1 

return -1 

# Printing the searched element using binary search

arr1 = [7, 8, 10, 2, 4, 80]

target1 = 80 # element to search 

# find the target

result1 = bs_recursive(arr1, 0, 5, target1)

print(f"The element found using the Binary Search iterative approach is at index: {result1}")

 
arr2 = [7, 8, 10, 2, 4, 80]

target2 = 10 # element to search
 

# find the target

result2 = bs_iterative(arr2, target2)

print(f"The element found using the Binary Search recursive approach is at index: {result2}")
