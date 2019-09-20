import random
#print(random.sample(range(20),10))

sum=0
aver=0
length=0

for element in random.sample(range(20),10):
    print("Random list of element, № ", length ,": ", element)
    sum += element
    length +=1

print("Sum of element: ", sum)

aver = sum/length
print("Avarege of element: " , aver)
