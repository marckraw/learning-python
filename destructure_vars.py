x = 4, 11 # brackets are not neccessary
z = [(4, 11)] # when in list, you NEED parantheses


x, y = 4, 11 # destructure


t = 5, 11
d, z = t


some_stuff = ("Bob", 23, "Mechanic")
name, _, profession = some_stuff


#const [head, ...tail] = [1,2,3,4,5] - in javascript
head, *tail = [1,2,3,4,5] # head = 1, tail = [2,3,4,5]
*something, last = [1,2,3,4,5] # something = [1,2,3,4,], last = 5
print(tail)
print(*tail) # this will not print array, but 2 3 4 5 which is perfectly valid python