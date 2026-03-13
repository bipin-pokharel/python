# users = ["Dave", "John", "Sara"]

# data = ["Dave", 42, True]

# emptylist = []

# print("Dave" in users)
# print(users[0])
# print(users[-1])
# print(users[-2])

# print(users.index("Sara"))
# print(users[0:])

# print(len(data))
# users.append("Elsa")
# print(users)

# users += ["Sason"]
# print(users)

# users.extend(["Robert", "Jimy"])
# print(users)

# users.extend(data)
# print(users)

# users.insert(0, "Bob")
# print(users)

# users[2:2] = ["Eddie", "Alex"]
# print(users)

# users[1:3] = ["Robert", "JPJ"]
# print(users)

# users.remove("Bob")
# print(users)
# print(users.pop())
# print(users)

# del users[0]
# print(users)

# del data
# data.clear()
# print(data)

# users[1:2] = ["Dave"]
# users.sort()
# print(users)
# users.sort(key=str.lower)
# print(users)

# nums = [4, 42, 54, 5, 67]
# nums.reverse()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]
# print(numscopy)
# print(mynums)
# mycopy.sort()
# print(mycopy)

# print(type(nums))

# mylist = list([1, "bipin", True])
# print(mylist)


# tuples
mytuple = tuple(("dave", 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))
print(anothertuple)


newlist = list(mytuple)
newlist.append("neil")
newtuple = tuple(newlist)
print(newtuple)


(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
