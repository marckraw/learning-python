

# while user_input != "n": while True
#   print("Do something")



friends = ["Rolf", "Jen", "Bob"]

for friend in friends:
    print(friend)

for friend in range(3):
    print(friends[friend])



grades = [32, 32, 41, 213, 45]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)


total_with_sum = sum(grades)
print(total_with_sum)