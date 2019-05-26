f=open('example.txt','w')
print('File Opened in write mode:\nWrite the text lines in it and to end press -1')
t=input()
while t!='-1':
    f.write(t+'\n')
    t=input()
f.close()
print('File opened in read mode:')
f=open('example.txt','r')
n=0
for line in f:
    words=line.split()
    n+=len(words)
f.close()
print('The number of words in the file is',n)
