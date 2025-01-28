class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and earns {self.salary}'
    
class Manager(Employee):
    title = 'Manager'
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
        
    def __str__(self):
        return super().__str__() + f' working in {self.department} as a {self.title}'
    
class Executive(Manager):
    title = 'Executive Manager'
    def __init__(self, name, age, salary, department, bonus):
        super().__init__(name, age, salary, department)
        self.bonus = bonus
        
    def __str__(self):
        return super().__str__() + f' with a bonus of {self.bonus}'
    
    
baseSalary = 50000
mMultiplier = 1.4
eMultiplier = 1.8
bonusAmount = baseSalary * 0.2
    
e1 = Employee('Amy', 29, baseSalary)
print(e1)
e2 = Manager('Joel', 35, int(round(baseSalary*mMultiplier, 0)), 'Sales')
print(e2)
e3 = Executive('Caitlin', 42, int(round(baseSalary*eMultiplier, 0)), 'Marketing', int(bonusAmount))
print(e3)

employees = {
    'Kathy': Employee('Kathy', 26, baseSalary),
    'Dale': Manager('Dale', 39, baseSalary * mMultiplier, 'Deveopment'),
    'Micheal': Executive('Micheal', 37, baseSalary * eMultiplier, 'Account', int(bonusAmount))
} 
for x in employees:
    print(employees[x])