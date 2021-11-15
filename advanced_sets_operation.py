friends = {"Bob", "Rolf", "Anne"}
abroad = {"Adam", "Rolf"}


# Sets operations #
# ############### #
# Difference
local_friends = friends.difference(abroad) # checks difference between sets
print(local_friends)

# Union
sum_of_friends = friends.union(abroad) # union
print(sum_of_friends)

# Intersection
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)

