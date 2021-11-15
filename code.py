# String formatting
name = "Rolf"
greeting = f"Hello, {name}" # f before string, to input variables in { }
print(greeting)


# Temlate string with .format
greeting = "Hello, {}"
name = "Bob"
with_name = greeting.format(name)
with_name_two = greeting.format("something")
print(with_name)
print(with_name_two)

# Longer phrase
longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
