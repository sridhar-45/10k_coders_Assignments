#  1.WAP to print square pattern using nested loop.
def top_star_pyramid(n):
    """Creates a centered star pyramid"""
    print("Star Pyramid:")
    for i in range(1, n + 1):
        # Print spaces for centering
        spaces = ' ' * (n - i)
        # Print stars
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def bottom_star_pyramid(n):
    for i in range(n, 0, -1):
        # Print spaces for centering
        spaces = ' ' * (n - i)
        # Print stars
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()    
        

top_star_pyramid(5)   
bottom_star_pyramid(5)
