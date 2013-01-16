import zipfile

zf = zipfile.ZipFile('channel.zip')
zc = []
name = '90052.txt'

while True:
    f = open('channel/%s' % name)
    data = f.read().split()[-1]
    f.close()
    zc.append(zf.getinfo(name).comment)
    if data.isdigit():
        name = '%s.txt' % data
    else:
        break
print ''.join(zc)
