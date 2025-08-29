# 1. Dictionaries:
#     car_info = {
#         "brand" : "Tesla",
#         "mdoel" : "Models",
#         "price" : "1.5cr",
#         "features" : ["Autopilot", "Electric", "Sunroof"]
#     }
    
#     - Add "color" : "white"
#     - update "price" to "1.7cr"
#     - Add nested key "insurance" with {"Provider":"HDFC", "valid_till" : "2026"}
    
    
car_info = {
        "brand" : "Tesla",
        "mdoel" : "Models",
        "price" : "1.5cr",
        "features" : ["Autopilot", "Electric", "Sunroof"]
    }


#adding the new key :value
car_info["color"] = "White"


#update the dict
car_info["price"] = "1.7cr"


#adding nested key...
for key, val in {"Provider":"HDFC", "valid_till" : "2026"}.items():
    car_info[key] = val
print(car_info)    












# 2. Nested Dictionary Print:
#     laptop = {
#         "brand" : "Apple",
#         "spaces" : {"ram":"16gb", "storage": "1TB SSD", "chip":"M2"},
#         "price" : "2L"
#     }
#     - print "chip" value
#     - print : Apple laptop comes with M2 chip and costs 2L.
#     }


laptop = {
        "brand" : "Apple",
        "spaces" : {"ram":"16gb", "storage": "1TB SSD", "chip":"M2"},
        "price" : "2L"
    }
    
#  print "chip" value
chip_val = laptop["spaces"]["chip"]
print(val)

#print : Apple laptop comes with M2 chip and costs 2L.
print(f"{laptop["brand"]} laptop comes with {val} chip an costs {laptop["price"]}")
