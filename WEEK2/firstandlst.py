def binary_search(arr, x1,x2): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x1: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x1: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x1,x2=2,10
  
# Function call 
result = binary_search(arr, x1,x2) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array")