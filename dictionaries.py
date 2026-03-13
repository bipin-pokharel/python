#  Dictionaries
band = {"vocals": "plant", "guitar": "page"}
band2 = dict(vocals="plant", guitar="page")
print(band)
print(band2)
print(type(band))
print(type(band2))
print(len(band))

# Access items in the dictionary
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list pf key value pair as tuples
print(band.items())

# verify if key exists
print("guitar" in band)
print("triangle" in band)

# change values in dictionary
band["vocals"] = "coverdale"
band.update({"bass": " JPJ"})
print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bohnam"
print(band)
print(band.popitem())  # only teturns the value in terminal
print(band)

# Delete and clear
band["drums"] = "bohnam"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2

# Copy dictionary
# band2 = band  # crate a reference
# print("bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Bipin"
# print(band)

band2 = band.copy()
band2["drums"] = "bipin"
print("good copy")
print(band)
print(band2)
