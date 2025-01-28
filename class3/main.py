import math #if you want to use math library

class Car:
    
    # def __init__(self, color='white', num_wheels=2): #initilizer 
    def __init__(self, color: str, num_wheels: int): #initilizer 
        if not color or not num_wheels:
            raise ValueError('Color and Number of wheels must be required')
        
        if num_wheels <= 0:
            raise ValueError('Number must be more than 0')
             
        self.color = color
        self.number_of_wheels = num_wheels
        
    
    def increase_wheels(self):
        print(self.color) #same as "this" in JS
        self.number_of_wheels += 1
        
    def __str__(self):
        return "Hello I am a car"
        
c1 = Car('red', 3)
print(c1.color, c1.number_of_wheels) #red 3
# c1.color = 'red'

c2 = Car('blue', 4)
print(c2.color, c2.number_of_wheels) #blue 4

# c3 = Car(None, 0)
# print(c3.color, c3.number_of_wheels) #return initial value

# c3 = Car('Pink', -1)


##-----
class Person:
    status = 'Person' 
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f'Hi, I am a {self.status} named {self.fname} {self.lname}'
    
    
class Student(Person):
    status = 'Student'
    def __init__(self, fname, lname, student_id):
        super().__init__(fname, lname)
        self.student_id = student_id
        
    def __str__(self):
        return super().__str__() + f', student id is {self.student_id}.'
    
class Teacher(Person):
    status = 'Teacher'
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject
        
    def __str__(self):
        return  super().__str__() + f', teaching {self.subject}.'
        
    
s1 = Student('Rika', 'Sonohara', 'CCTB80083')
print(s1) #Hi, I am a Person named Rika Sonohara, student id is CCTB80083

t1 = Teacher('Aryan', 'Arora', 'Python')
print(t1)

print(getattr(t1, 'subject'))

#1. get all attributes of t1 <- this one is easire
for key, value in t1.__dict__.items():
    print(key, value)
    
#2. get all attributes of s1 
for att in dir(s1):
    print(att, getattr(s1, att))
    
print(dir(s1)) # -- only can get all properties, not values

print('------MRO(MEthod order resolution)-------')
class A:
    def __str__(self):
        return f'in class A'
    
class B(A):
    def __str__(self):
        return f'in class B'
    
class C(A):
    pass

class D:
    def __str__(self):
        return f'in class D'
    
class E(A, D):
    pass

class G(C, D):
    pass
    
o1 = A()
o2 = B()
o3 = C()
o4 = D()
o5 = E()
o6 = G()

print(o1) #in class A
print(o2) #in class B
print(o3) #in class A
print(o4) #in class D
print(o5) #in class A  <-- check the order of inheritance, it is E(itself), A(firs parent), D(second parent)  
print(o6) #in class A  <-- class C is the first parent and it has A as its parent
 
 
print('------Error handling-------')
def test_func():
    try:
        print('test')
        #i.g ... update record in database
        #1: update username: NAME
        
        #2: update email: FAILS(get error)
        
    except: 
        print('Invalid input')
        # UNDO EVERYTHING: 1&2
        
def test_func2():
    try: 
        try: 
            raise TypeError('type is not correct')
        except:
        # except Exception as e:
            # print(f'Error: {e}') #Error: type is not correct
            raise
    except Exception as e:
        print(e) #type is not correct


test_func2()