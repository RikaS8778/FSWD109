#booleans
print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# Get all students from the database
def students():
    #return ['s1','s2','s3','s4','s5']
    return []

student = students()

if student:
    print("Students are presented")  
    print(student[0]) #when list is empty, it will throw an error(IndexError)
else:
    print("No students are presented")
    

# ---

a = 10
print(isinstance(a, int)) #True
print(isinstance(a, str)) #False

def add(a: int, b: int) -> int:
    isAint = isinstance(a, int)
    isBint = isinstance(b, int)
    if not isAint or not isBint:
        raise TypeError('Both arguments should be integers')
        return
    return a + b

print(add(10, 20))
# print(add(10, 20.5)) #return 30.5 we need to add error handling by myself
#print(add(10, '20')) #typeError

# in python, we can't use expromation mark(!) instead of 'not'

# ---
a = True
b = False
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")
    
# **= is the power operator
a = 3
b = a ** 3
print(b) #27

#---
numbers = [1, 2, 3, 4, 5]

if 0 not in numbers:
    print("0 is NOT in the list")
else:
    print("0 is in the list")
    
for n in numbers:
    print(n)
    
# ---
numbers = [1, 2, 3, 4, 5]
numbers_ext = [6, 7, 8, 9, 10]

numbers.extend(numbers_ext) #modified the original list

print(numbers) 

# ---
numbers = ["s1", "s2", "s3", "s3", "s4", "s5", "s5"]

def remove_duplicates(numbers: list) -> list:
    return sorted(list(set(numbers)))

print(remove_duplicates(numbers))


# ---
students =  ["s1", "s2", "s3", "s3", "s4", "s5", "s5"]
students_2 =  ["s3", "s1", "s2", "s3", "s3", "s4", "s3", "s3", "s3", "s5"]

# ---my solution start---
def removeStudentFromList(students: list[str], name: str) -> list[str]:
    students_new = []
    for student in students:
        if student != name:
            students_new.append(student)
    return students_new

students_without_s3 = removeStudentFromList(students_2, "s3")
print(students_without_s3)

# ---my solution end---

# ---other solution start---
def removeStudentFromList_1(students: list[str], name: str) -> list[str]:
    num = students.count(name)
    # -- 1st solution
    for i in range(num):
        students.remove(name)
    return students

    # -- 2nd solution
    while name in students:
        students.remove(name)
    return students
students_without_s4 = removeStudentFromList_1(students_2, "s3")
print(students_without_s4)
# ---other solution end---
