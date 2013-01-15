text = ''
with open('text') as file:
  for line in file:
    text += line
    
print ''.join(x for x in text if x.isalpha())
