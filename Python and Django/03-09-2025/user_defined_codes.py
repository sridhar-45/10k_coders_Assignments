"""
Custom String Functions (User-defined)
Author: Sridhar Goudu
Description: User-defined implementations of common Python string functions:
swapcase, strip, lstrip, rstrip, count, replace
"""

# ------------------ 1. swapcase() ------------------
# Converts uppercase letters to lowercase and lowercase letters to uppercase
def custom_swapcase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char  # leave non-alphabetic characters unchanged
    return result

# Example usage
print("swapcase():", custom_swapcase("Hello World!"))  # 'hELLO wORLD!'


# ------------------ 2. strip(), lstrip(), rstrip() ------------------
# Removes whitespaces from both ends (strip), left end (lstrip), right end (rstrip)

def custom_strip(s):
    return custom_lstrip(custom_rstrip(s))

def custom_lstrip(s):
    start = 0
    while start < len(s) and s[start] in " \t\n\r":
        start += 1
    return s[start:]

def custom_rstrip(s):
    end = len(s) - 1
    while end >= 0 and s[end] in " \t\n\r":
        end -= 1
    return s[:end+1]

# Example usage
s = "   Hello World   "
print("strip():", custom_strip(s))   # 'Hello World'
print("lstrip():", custom_lstrip(s)) # 'Hello World   '
print("rstrip():", custom_rstrip(s)) # '   Hello World'


# ------------------ 3. count() ------------------
# Counts the number of occurrences of a substring in the string

def custom_count(s, sub):
    n = len(s)
    m = len(sub)
    if m == 0:
        return n + 1  # empty substring occurs n+1 times
    count = 0
    for i in range(n - m + 1):
        if s[i:i+m] == sub:
            count += 1
    return count

# Example usage
text = "banana"
print("count('a'):", custom_count(text, "a"))   # 3
print("count('na'):", custom_count(text, "na")) # 2


# ------------------ 4. replace() ------------------
# Replaces all occurrences of old substring with new substring

def custom_replace(s, old, new):
    result = ""
    i = 0
    n = len(s)
    m = len(old)
    
    if m == 0:  # if old is empty string, insert new between every character
        for char in s:
            result += new + char
        result += new
        return result
    
    while i < n:
        # Check if old substring matches at position i
        if s[i:i+m] == old:
            result += new
            i += m
        else:
            result += s[i]
            i += 1
    return result

# Example usage
text2 = "I like Python. Python is fun."
print("replace('Python', 'Java'):", custom_replace(text2, "Python", "Java"))
# 'I like Java. Java is fun.'
