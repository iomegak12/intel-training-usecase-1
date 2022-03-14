import re

string = 'Twelve:12 Eighty \
        one more thing \
     nine:89 i am really good and super hero like batman487 superman7'
pattern = '\d+'

result = re.split(pattern, string)

print(result)