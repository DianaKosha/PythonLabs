import random

a=0
c=0

for i in random.sample(range(50),7):
    a += i
    c +=1

print(a) #sum
 b=0
b = a/c #aver
print(b)
