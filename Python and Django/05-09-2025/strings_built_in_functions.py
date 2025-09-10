"""
Python String Built-in Functions
Author: Sridhar Goudu
Description: Examples and usage of various Python string built-in functions,
including common and lesser-known functions like partition, swapcase, isidentifier, casefold, removeprefix, etc.
"""

# ------------------ Basic String Functions ------------------

s = " Hello World "

# 1. upper() - converts all letters to uppercase
print("upper():", s.upper())  # ' HELLO WORLD '

# 2. lower() - converts all letters to lowercase
print("lower():", s.lower())  # ' hello world '

# 3. title() - capitalizes the first letter of each word
print("title():", s.title())  # ' Hello World '

# 4. capitalize() - capitalizes only the first character of the string
print("capitalize():", s.capitalize())  # ' hello world '

# 5. strip() - removes leading and trailing whitespaces
print("strip():", s.strip())  # 'Hello World'

# 6. lstrip() - removes leading whitespaces
print("lstrip():", s.lstrip())  # 'Hello World '

# 7. rstrip() - removes trailing whitespaces
print("rstrip():", s.rstrip())  # ' Hello World'

# 8. split() - splits string into a list by separator
print("split():", s.split())  # ['Hello', 'World']

# 9. rsplit() - splits string from right
print("rsplit():", s.rsplit())  # ['Hello', 'World']

# 10. join() - joins iterable elements into string using s as separator
words = ["Python", "is", "fun"]
print("join():", " ".join(words))  # 'Python is fun'

# ------------------ Numeric Checks ------------------

num_str = "123"
print("isnumeric():", num_str.isnumeric())  # True
print("isdigit():", num_str.isdigit())      # True
print("isdecimal():", num_str.isdecimal())  # True

# ------------------ Case and Swap ------------------

text = "Python is FUN"
print("swapcase():", text.swapcase())  # 'pYTHON IS fun'
print("casefold():", text.casefold())  # 'python is fun'

# ------------------ Partition ------------------

text2 = "hello_world_python"
print("partition():", text2.partition("_"))  # ('hello', '_', 'world_python')
print("rpartition():", text2.rpartition("_"))  # ('hello_world', '_', 'python')

# ------------------ Justification and Filling ------------------

s2 = "Hi"
print("center(6, '*'):", s2.center(6, "*"))  # '**Hi**'
print("ljust(5, '-'):", s2.ljust(5, "-"))    # 'Hi---'
print("rjust(5, '-'):", s2.rjust(5, "-"))    # '---Hi'
print("zfill(5):", s2.zfill(5))              # '000Hi'

# ------------------ Encoding ------------------

s3 = "hello"
b = s3.encode()
print("encode():", b)  # b'hello'

# ------------------ Identifier and ASCII Checks ------------------

id1 = "my_var"
id2 = "123abc"
print("isidentifier() id1:", id1.isidentifier())  # True
print("isidentifier() id2:", id2.isidentifier())  # False

uni = "hello"
non_ascii = "हैलो"
print("isascii() uni:", uni.isascii())           # True
print("isascii() non_ascii:", non_ascii.isascii()) # False

# ------------------ Remove Prefix/Suffix ------------------

word = "unhappy"
filename = "document.txt"
print("removeprefix('un'):", word.removeprefix("un"))   # 'happy'
print("removesuffix('.txt'):", filename.removesuffix(".txt"))  # 'document'

# ------------------ Expand Tabs ------------------

text_tab = "a\tb\tc"
print("expandtabs(4):", text_tab.expandtabs(4))  # 'a   b   c'

# ------------------ Startswith / Endswith ------------------

s4 = "hello.py"
print("startswith('he'):", s4.startswith("he"))  # True
print("endswith('.py'):", s4.endswith(".py"))    # True

# ------------------ Count and Find ------------------

s5 = "banana"
print("count('a'):", s5.count("a"))  # 3
print("find('na'):", s5.find("na"))  # 2 (first occurrence)
print("rfind('na'):", s5.rfind("na")) # 4 (last occurrence)

# ------------------ Index ------------------

print("index('na'):", s5.index("na"))  # 2
# print(s5.index("xyz"))  # would raise ValueError

# ------------------ isalpha / isalnum / isspace ------------------

s6 = "Python"
s7 = "Python123"
s8 = "   "
print("isalpha():", s6.isalpha())   # True
print("isalnum():", s7.isalnum())   # True
print("isspace():", s8.isspace())   # True

# ------------------ Replace ------------------

s9 = "I like Python"
print("replace('Python', 'Java'):", s9.replace("Python", "Java"))  # 'I like Java'

# ------------------ Partition & rpartition Review ------------------

text3 = "key=value=other"
print("partition('='):", text3.partition("="))  # ('key', '=', 'value=other')
print("rpartition('='):", text3.rpartition("="))  # ('key=value', '=', 'other')

# ------------------ Additional Examples ------------------

text4 = "abcDEF123"
print("isalnum():", text4.isalnum())  # True
print("isupper():", text4.isupper())  # False
print("islower():", text4.islower())  # False
print("istitle():", text4.istitle())  # False

# ------------------ Any and All with Strings ------------------

chars = ['a', 'b', '', 'd']
print("any(chars):", any(chars))  # True (non-empty elements exist)
print("all(chars):", all(chars))  # False (there is an empty string '')

# ------------------ Reverse string ------------------

s_rev = "hello"
print("reversed string:", ''.join(reversed(s_rev)))  # 'olleh'
