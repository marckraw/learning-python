# associate keys and values together
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Anne"] = 50 # changing value of key

dupa = friend_ages["Adam"] # ids will not work here
print(dupa)




friends = [
    {
        "name": "Rolf",
        "age": 24
    },
    {
        "name": "Adam",
        "age": 40
    },
    {
        "name": "Anne",
        "age": 60
    }
]

print(friends[1]["name"])


# you can also for in dictionary

students_attendance = {"Rolf": 98, "Bob": 80, "Anne": 100}

for student, attendance in students_attendance.items():
    print(f"{student}: {students_attendance[student]}")

if "Bob" in students_attendance:
    print("Bob is attendance")

attendance_values = students_attendance.values()
print(attendance_values)