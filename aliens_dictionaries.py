# Dylan Nelson
# February 12, 2024
# dictionary_intro.py

# A dictionary is created using the curly brackets {},
# dictionaries are great for storing multiple different, 
# parameters to a variable

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'], alien_0['points'])

new_points = alien_0['points']

print(f'You just earned {new_points} points!')

# adds new key-value points to the dictionary, these are the coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# prints out all the associated data with the alien_0
print(alien_0)
