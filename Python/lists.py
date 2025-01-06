# Define the list of names
names = ["Henry", "Chris", "Tom", "Ricardo"]

print(names[2])

# lists are mutable
names.append("Luca") # append() can only add one item at a time

names.extend(["Andrea", "Michka", "Wayne"]) # extend() method allows you to add multiple items to a list.

names.sort() # sorts the list

print(names)
