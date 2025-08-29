# 1. List Practice
# players = ["Rohit", " virat", "Gill", "Dhoni"]
# - Replace "Gill" with "surya"
# - Add "Jadeja" at the end
# - Print the length and second last player

players = ["Rohit", " virat", "Gill", "Dhoni"]
print(players)
pos = players.index("Gill")
players[pos] = "Surya"
print(players)






# 2. Tuple Practice:
# - laptop_info = ("HP", "16Gb", "512gb SSD", 2024, True)
# - Try modifying one value - explain the result
# - Acess and print the last 2 elements

laptop_info = ("HP", "16Gb", "512gb SSD", 2024, True)
### we can't modify the tuple , because tuples are immutable datatypes
last_sec = laptop_info[-2]
last_one = laptop_info[-1]
print(last_sec)
print(last_one)





# 3. Set Practice:
#     countries = {"india", "USA", "india", "canada". "UK", "USA"}
#     Print the set(observe duplicates)
#     add "Germany" , remove "UK"

countries = {"india", "USA", "india", "canada", "UK", "USA"}
print(countries) # set consists only unique elements and non-ordering of elements
countries.add("Germany")
print(countries)
countries.remove("UK")
print(countries)







# 4. Frozenset Practice:
#     frozen_marks = frozenset([90,85,75,85])
#     -try to add or remove the values and observe the error
#     - print its types
    
frozen_marks = frozenset([90,85,75,85]) #A frozenset is an immutable version of a set.   
print(frozen_marks)
# frozen_marks.add(100)   # Error: 'frozenset' object has no attribute 'add'
 #frozen_marks.remove(85) # Error: 'frozenset' object has no attribute 'remove'




    
