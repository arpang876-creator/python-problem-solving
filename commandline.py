

'''
list=[1,2,3]
sum=0
for i in range(0,len(list)):
    sum+=list[i]
print(sum)
'''


#command line argument
'''import sys
l = sys.argv
sum = 0
for i in range(1, len(l)):
    sum += int(l[i])
print(sum)
'''

import sys
args = sys.argv
for i in range(1, len(args)):
    print(args[i])
print(args[1])