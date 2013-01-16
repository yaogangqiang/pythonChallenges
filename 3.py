import re

text = ""
with open('3_text') as file:
    for line in file:
        text += line

p = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

print ''.join(p.findall(text))
