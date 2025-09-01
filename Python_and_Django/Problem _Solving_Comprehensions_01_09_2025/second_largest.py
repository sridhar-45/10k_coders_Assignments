def findSecondLargest(arr):
    
    if len(arr) < 2:  #base condition
        return arr[0]
        
    if len(arr) == 2 : # arr contains only 2 elements
        if arr[0] < arr[1]:
            return arr[0]
        else:
            return arr[1]
            
    first_largest = arr[0]
    second_largest = arr[0]
    
    for val in arr:
        if val > first_largest:
            second_largest = first_largest
            first_largest = val
        elif val > second_largest and val != first_largest:
            second_largest = val
    
    return second_largest

arr1 = [-10,-10,-13,-2,-2,-9]
arr2 = [10, 10, 13, 2, 3, 9]
res = findSecondLargest(arr1)
print("second largest in negative values" , res)

op = findSecondLargest(arr2)
print("second largest in positive values ", op)

    
