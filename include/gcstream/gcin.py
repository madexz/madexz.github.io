import os
try:
    os.system('del return.txt')
except:
    pass

b = input()
a = open('return.txt','w')
a.write(b)
a.close()
