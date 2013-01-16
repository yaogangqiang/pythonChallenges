import pickle

f = open('banner.p')
for line in pickle.load(f):
    print ''.join(x[0] * x[1] for x in line) 
f.close()
