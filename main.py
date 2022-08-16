f=open('myfile.txt','a')
f.write('learning file handeling.')
f.close()
f=open('myfile.txt','r')
l=f.readlines()
for i in l:
    print(i)
f.close()