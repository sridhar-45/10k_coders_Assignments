def star_pyramid(n):
    """Creates a centered star pyramid"""
    print("Star Pyramid:")
    for i in range(1, n + 1):
        # Print spaces for centering
        spaces = ' ' * (n - i)
        # Print stars
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

star_pyramid(5)    
