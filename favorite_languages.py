# Dylan Nelson
# February 13, 2024
# favorite_languages.py

# This program will show how to call on the specific key or value

favorite_languages = {
    'james': 'rust',
    'dylan': 'Python',
    'mark': 'c',
    'sally': 'Assembly',
    'lane': 'Assembly',
    'briana': 'haskell'
}

# adds a list that contains a list of friends, so they get a custom message.
friends =['dylan', 'briana', 'lane', 'james']

# # the values can be simple n and l for looping
# for n, l in favorite_languages.items():
#     print(f"{n.title()}'s favorite language is {l.title()}.")
#     if n in friends:
#         print(f"Hello {n.title()}! Nice to see you :D")

# # Using only the first item in the key-value pair
# for n, l in favorite_languages.items():
#     print(f"{n.title()} is a person who casted their vote.")
# # Using the second item in the key-value pair
# for n, l in favorite_languages.items():
#     print(f"One programming language is {l.title()}.")

# Using only the key items in the key-value pair
for names in favorite_languages.keys():
    print(f"{names.title()} is a person who casted their vote.")
    if names in friends:
        print(f"Hello {names.title()}! Nice to see you :D")
# Using the value items in the key-value pair
for languages in favorite_languages.values():
    print(f"One programming language is {languages.title()}.")
