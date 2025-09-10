def custom_isalnum(s):
    # Empty string is not considered alphanumeric
    if len(s) == 0:
        return False
    
    for char in s:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')):
            return False
    return True

# Example usage
print(custom_isalnum("Python123"))  # True
print(custom_isalnum("Python_123")) # False (contains '_')
print(custom_isalnum(""))           # False (empty string)
