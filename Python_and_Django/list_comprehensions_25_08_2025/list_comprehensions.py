# Task:
# Create a list of factorials of the first 5 numbers using list comprehensions.
# Check previous and next numbers of given num is armstrong or not?


def fact(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return n * fact(n-1)   

nums = [1,4,5,2,7,8]
factorials = [fact(num) for num in nums]
print(factorials)
