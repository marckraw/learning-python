def divide(divident, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return divident / divisor


def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)

print(result)



####################

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not fing an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

def get_friend_name(friend):
    return friend["name"]


# print(search(friends, "Rolf Smith", get_friend_name))
# print(search(friends, "Bob Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"])) # with lambda