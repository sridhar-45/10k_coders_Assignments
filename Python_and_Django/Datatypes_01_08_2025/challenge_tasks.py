# 1. Movie Tracker:
#     ott_data =[
#         {"platform" : "Netflix", "shows" : ["Stranger Things", "wednesday"]},
#         {"platform" : "Prime", "shows" : ["Mirzapur" , "Farzil"]},
#         {"platform" : "Hotstar", "shows" : ["Special Ops", "The Freelancer"]},
#     ]
#     - Add a new show to prime
#     - print all shows in Netflix
    
ott_data = [
        {"platform" : "Netflix", "shows" : ["Stranger Things", "wednesday"]},
        {"platform" : "Prime", "shows" : ["Mirzapur" , "Farzil"]},
        {"platform" : "Hotstar", "shows" : ["Special Ops", "The Freelancer"]},
] 
    
    
# Add a new show to Prime
for platform in ott_data:
    if platform["platform"] == "Prime":
        platform["shows"].append("Family Man")

print(ott_data)
    

# Print all shows in Netflix
for data in ott_data:
