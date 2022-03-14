import re

pattern = '^a...s$'
string_input = 'abyss'

result = re.match(pattern, string_input)

if result:
    print('Search Succcessful!')
else:
    print('Search Not Successful')
