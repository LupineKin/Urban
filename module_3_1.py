<<<<<<< HEAD
﻿def count_calls():
=======
def count_calls():
>>>>>>> 0d3cd3d68f0dbc7f742f72885a3419b5c168c324
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = [len(string), string.upper(), string.lower()]
    a = tuple(a)
    return (a)

def is_contains(string, list_to_search):
    count_calls()
    a = False
    list_to_search = [b.lower() for b in list_to_search]
    if string.lower() in list_to_search:
        a = True
    return (a)


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
