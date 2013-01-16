text = ""
with open('2_text') as file:
    for line in file:
        text += line

num = {}
for i in text:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

def sortDict(Dict):
    return sorted(Dict.items(), key = lambda e:e[1])

sorted_list = sortDict(num)

for key, value in sorted_list:
    print "%s: %d" % (key, value)
