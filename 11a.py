from collections import defaultdict
d=defaultdict(int)
def names():
    while(1):
        n=input('Enter the first name: ')
        if n=='':
            break
        d[n]+=1
    for i in sorted(d.keys()):
        print('There are',d[i],'students named',i)
names()
