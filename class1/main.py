#############################
#  Class 1 - Python Basics  #
#############################


print('Hello World!')

# A variable can only hold one thing(type) at a time
x = 10
name = 'Rika'
is_student = True
y = 3.14

print(type(x))
print(type(name))
print(type(is_student))
print(type(y))

a = 10
b = 21
print(a + b)

# typeError
c = '10'
d = 21
# print(c + d)

e = 11
f = True
print(e + f)

# TODO:
# FIXME:


testGlobal = 10
def total_sales(sales: list) -> int:
    # global testGlobal #can overwrite the global variable
    # testGlobal = 20
    
    testGlobal = 100 #local variable
    
    print(testGlobal) 
    return sum(sales)

print(testGlobal)

print(total_sales([100, 200, 300, 400, 500]))

print(total_sales([100, "200", 300, 400, 500]))

x, y, z = 'orange', 'banana', 'apple'
print(x)
print(y)
print(z)

x = y = z = 'pineapple'
print(x)
print(y)
print(z)

fruits = ['apple', 'grape', 'cherry']
x, y, z = fruits
x = fruits[0]
y = fruits[1]
z = fruits[2]
print(x)
print(y)
print(z)

#Sequence Type: list tuple range
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
set = {1, 2, 3, 4, 5}
set_2 = {0, 1, 5, 6, 7}
set_3 = set.union(set_2)
print(set_3)
print(set.intersection(set_2)) #5, 1
print(set.difference(set_2))    #2, 3, 4
dict = {'one': 'apple', 'two': 'banana', 'three': 'cherry'}
dict_2 = {1: 'cat', 2: 'dog', 3: 'rion'}

set.update([2, 5, 8])
print(set)

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3) #{'microsoft', 'google', 'banana', 'cherry'}

#equal symmetric_difference
set5_1 = set1.intersection(set2)
set5 = set1.union(set2).difference(set5_1)
print(set5) #{'banana', 'google', 'microsoft', 'cherry'}


set4 = set1.difference(set2)
print(set4) #{'banana', 'cherry'}



range = range(6)
for i in range:
    print(i)

x = {
    'name': 'Rika',
    'height': 5.5,
    'is_student': True
}

print(type(x['name']))
print(x['name'])


"""
# This is a multi-line comment
# This is a multi-line comment
# This is a multi-line comment
"""

name = "Rika"
print(name[0])
print(name[0:3]) #Rik same as range(0, 3) name[start:end] slice end_point is not included
print(name[0:3:2]) #Rk

if 'R' in name:
    print('Yes')
else:    
    print('No')
    
letter = 'W'
hasLetter = letter in name 
if hasLetter:
    print('Yes')
else:    
    print('No')
    
print(name[-1:-5:-1]) #akiR
print(name[::-1]) #akiR

a = "  TE ST "
print(a.strip()) #TE ST rtrim/ltrim
print(a.strip().replace(' ', '')) #TEST

hobbies = 'reading,coding,gaming'
print(hobbies.split(',')) #['reading', 'coding', 'gaming']

#f-string
name = 'Rika'
program = 'Python'
print(f'Hello, my name is {name}! I am learning {program}')

x = 12
y = 6
print(f'The multiply of {x} and {y} is {x * y}')

#St.format()
print('Hello, my name is {name}! I am learning {program}'.format(name=name, program=program))

