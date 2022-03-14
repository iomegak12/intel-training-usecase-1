import re

string = '39801 356, 2102 1111'

pattern = '(\d{3}) (\d{2})'

result = re.search(pattern, string)

if result:
    print(result.group())

print('Understanding the difference between search and findall ...')

result = re.findall(pattern, string)

print(result)