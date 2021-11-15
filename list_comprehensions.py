numbers = [1, 3, 5]


doubled = [x * 2 for x in numbers] # list comprehension
print(doubled)




friends = ["Rolf", "Sam", "Samantha", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


starts_s_with_list_comprehension = [friend for friend in friends if friend.startswith("S")]
print(starts_s_with_list_comprehension)
print(id(starts_s_with_list_comprehension)) # reference of of this specific list in memory