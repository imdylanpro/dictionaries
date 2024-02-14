# Dylan Nelson
# February 12, 2024
# nested_dictionaries.py

# This program will give an example of using a dictionary within a dictionary

# alien_0 = {'color': 'green', 'points': 5, 'speed': 'fast'}
# alien_1 = {'color': 'purple', 'points': 15, 'speed': 'medium'}
# alien_2 = {'color': 'yellow', 'points': 25, 'speed': 'fast'}
# aliens = ['alien_0', 'alien_1', 'alien_2']

# for alien in aliens:
#     print(alien)
# print(f'You just earned {new_points} points!')

# Makes an empty list for storing aliens
aliens = []

# Makes a list of 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow',}
    aliens.append(new_alien)

# Using a slice the first 3 aliens are modified to be different
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'fast'

# The len function reports back the number of items in the list
print(f'The total number of aliens created is {len(aliens)}')
