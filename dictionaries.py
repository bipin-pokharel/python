#  Dictionaries
# band = {"vocals": "plant", "guitar": "page"}
# band2 = dict(vocals="plant", guitar="page")
# print(band)
# print(band2)
# print(type(band))
# print(type(band2))
# print(len(band))

# Access items in the dictionary
# print(band["vocals"])
# print(band.get("guitar"))

# list all keys
# print(band.keys())

# list all values
# print(band.values())

# list pf key value pair as tuples
# print(band.items())

# verify if key exists
# print("guitar" in band)
# print("triangle" in band)

# change values in dictionary
# band["vocals"] = "coverdale"
# band.update({"bass": " JPJ"})
# print(band)

# remove items
# print(band.pop("bass"))
# print(band)

# band["drums"] = "bohnam"
# print(band)
# print(band.popitem())  # only teturns the value in terminal
# print(band)

# Delete and clear
# band["drums"] = "bohnam"
# del band["drums"]
# print(band)
# band2.clear()
# print(band2)
# del band2

# Copy dictionary
# band2 = band  # crate a reference
# print("bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Bipin"
# print(band)

# band2 = band.copy()
# band2["drums"] = "bipin"
# print("good copy")
# print(band)
# print(band2)

# or use the dict() constructor function
# band3 = dict(band)
# print("good copy")
# print(band3)

# nested dictionaries
member1 = {"name": "plant", "instrument": "vocals"}
member2 = {"name": "page", "instrument": "guitar"}
band = {"member1": member1, "member2": member2}
print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4, 5}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 4}
print(nums)

# true is a dupe of 1 ,fale is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a vlaue is is a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new elemnt to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with tupkes with lists ,tuples and dictionaries ,too

# Merge two set to create new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
