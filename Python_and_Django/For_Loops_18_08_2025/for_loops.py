# 1.Print numbers from 100 to 0 in reverse which are divisible by 5 
for i in range(100, 0):
  if i % 5 == 0:
    print(i)


# 2. Check whether given string is a palindrome or not using a function
def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
string1 = "madam"
string2 = "Hello"

print(f"{string1} is Palindrome? ->", is_palindrome(string1))
print(f"{string2} is Palindrome? ->", is_palindrome(string2))





# 3. Write a function to print tables in reverse 
# for eg: 
#     3x10=30 
#     3x9=27
#     3x8=24

def reverse_table(n):
    for i in range(10, 0, -1):   # start from 10 and go down to 1
        print(f"{n} x {i} = {n * i}")

# Example usage
reverse_table(3)


