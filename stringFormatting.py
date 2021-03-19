age=34
print(f"You are {age}")
age = 44
print(f"You are {age}")

name = 76
print(f"This is number {name}")
name = 26 
print(f"Number {name}") # remember using the f formatting you can change variables.

for_example = 1, 2, 3, 4, 5
print(f"I am counting {for_example}")

name = "Joseph"
print(f"how are you {name}")
name = "Tambe"
print(f"how are you {name}")
name = "ability"
print(f"How are your {name}")
name = "NOBILItY"
print(f"How are your {name}")

name = "name"
print(f"I don't have a {name}")

age = 45
master =  str(age)
print("I am" + master)
print(f"i am {master}")
print("I am " + master)


name = 'Jose'
greeting = 'Hello, ' + name
print(greeting)

another_greeting = f'How are you, {name}?'
print(another_greeting)

name = 'Jose'
friend = 'Rolf'
phrase = name + ' is friends with ' + friend
print(phrase)

name = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"
 
address = f"""Name: {name}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
 
print(address)


description = "{} is {} years old."
print(description.format("Bob", 30))


description = "{} is {age} years old."
print(description.format("Bob", age=30))