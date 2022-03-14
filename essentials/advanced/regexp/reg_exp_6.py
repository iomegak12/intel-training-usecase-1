import re

# r prefixed pattern means raw string

string = '\n and \r are escape characters \f in any programming language'

result = re.findall(r'[\n\r]', string)

print(result)