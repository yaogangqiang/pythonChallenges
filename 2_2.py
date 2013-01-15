text = ""
with open('text') as file:
    for line in file:
        text += line

result = ""
for i in text:
    if i.isalpha():
        result += i

print result

