def second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None


def second_smallest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    
    return second if second != float('inf') else None


# Example
arr = [10, 20, 4, 45, 99, 4, 10]

print("Second Largest:", second_largest(arr))   # Output: 45
print("Second Smallest:", second_smallest(arr)) # Output: 10
