
num1 = 10 #integer
print(num1)

num2 = 20.5 #float value
print(num2)

num3 = 3+5j # complex 
print(num3)

bool1 = True#
print(type(bool1))

list1 =[2,3,5,7]
print(type(list1))
print(list[0])

tup1 =(2,3,4,(3,6))
print(type(tup1))

print(range(1,11))
print(list(range(1,11)))

str1 ="sandhya"
print(str1)

set1 ={2,3,4,5,6,7,8}
print(set1)

dict1 ={1:'sandhya',2:'10k coders',3:'python'}
print(dict1[3])

# operators
num1 = 5
num2 = 10
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 / num2)
# relational operators
print(3>5)#false
print(3==5)#false
print(3<4)
print(2<=6)
print(7>=4)
print(2!=6) #true
# logical operators
print(2 and 3)#3
print(0 and 4)#0
print(True or False)
print(-1 or -7)
#bitwise operator
print(2 & 3)#and operation
print(2 | 3)#or
print(2 ^ 3)#xor
print(2, ~ 3)
print(89 << 2)#left shift
print(76 >> 3)#right shift
#conditional statements
age= 20
if age > 18:
    print('you can vote')
else:
    print('you are minor,you can not vote')   
# for loop
for cls in range(1,11):#to print classes 1 to 10
    for roll in range(1,16):#to print roll no 1 to 15
        print(cls,roll)
#while loop to adding the numbers and come from the loop when it is 0
total = 0
number1 = int(input("enter a number to add and ('0 to quit')"))
while number1 != 0:
    total =total + number1
    number1 = int(input("enter a number and (0 to quit)"))
print(total)


    


#break
for i in range(0,11):
    print(i)
    if i == 5:
        break

for j in range(0,11):
    print(j)
    if j == 5:
        break#only loop terminated
    print(j)
#continue
for k in range(1,11):
    print(k)
    if k > 4:
        continue#only after contineous iterations are skipped
    print(k)
#function
def example(x,y):
    res = x+y
    print(res)    
example(2,3)    
#return statement
def find_gretest(a,b):
    if a > b:
        return a
    else:
        return b    

print(find_gretest(49,45))

