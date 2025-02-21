favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# loop through key values in a dictionary
# the variable name can be anything

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())
print('key-values'.center(20, '#'))

# looping through values
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")
print()

# looping through keys and values
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}")