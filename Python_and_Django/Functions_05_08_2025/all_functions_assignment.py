# Task:
# practise all types of function syntaxes and simple examples in a document


# 1. Basic Function (No Parameters, No Return)
def greet():
    print("Hello, Welcome to Python!")

greet()



  
# 2. Function with Parameters 
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Sridhar")




# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)




# 4. Function with Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sridhar")




# 5. Function with Keyword Arguments
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=22, name="Sridhar")



# 6. Function with Arbitrary Arguments *args
def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(90, 85, 75)




# 7. Function with Arbitrary Keyword Arguments **kwargs
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Sridhar", age=22, course="Python")




# 8. Function Returning Multiple Values
def calc(a, b):
    return a+b, a-b, a*b

s, d, p = calc(10, 5)
print("Sum:", s, "Diff:", d, "Product:", p)




#9. Anonymous Function (Lambda)
square = lambda x: x*x
print("Square of 6:", square(6))






# 10. Nested Function
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()




# 11. Function as Argument
def apply(func, value):
    return func(value)

result = apply(lambda x: x**3, 4)
print("Cube:", result)





# 12. Function Returning Another Function (Closure)
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print("Double of 5:", double(5))



# 13. Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))





# 14. Higher-Order Functions (map, filter, reduce)
from functools import reduce
# map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print("Squares:", squares)

# filter
evens = list(filter(lambda x: x%2==0, nums))
print("Evens:", evens)

# reduce
sum_all = reduce(lambda x,y: x+y, nums)
print("Sum:", sum_all)
