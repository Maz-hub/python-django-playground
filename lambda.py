# DICTIONARY INSIDE THE LIST

people = [
    {'name': 'Vita', 'departement': 'Development'},
    {'name': 'Namhee', 'departement': 'Sports'},
    {'name': 'Stephanie', 'departement': 'GMS'}
    ]
    
# SORT all the people and print them out

#sort by name
# this function is so simple and is only used in one place.
"""
def f(person):
    return person['name']

people.sort(key=f)
    """

# Python actually gives us an easier way to represent
# a very short, one-line function using something called a lambda expression.
# And this is a way of including the function just
# as a single value on a single line.

people.sort(key=lambda person: person['name'])


print(people)