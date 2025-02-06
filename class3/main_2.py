"""
Practice Question

• Suppose you are developing a system to manage different types of employees in a company.

• There are three types of employees: Employee, Manager, and Executive.

• An Employee has attributes name, age, and salary.

• A Manager is an Employee with an additional attribute department.

• An Executive is a Manager with an additional attribute bonus.

 

Implement these classes using inheritance in Python.

• Write methods to:

• Initialize the attributes of each class.

• Display information about each type of employee.

• Calculate the total earnings for each employee considering salary and bonus (if any).

• Provide a method to change the salary for an Employee.
"""



baseSalary = 50000
# mMultiplier = 1.4
# eMultiplier = 1.3
bonusAmount = baseSalary * 0.2

class Employee:
    multiplier = 1.0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and earns {self.calc_salary()}'
    
    def calc_salary(self):
        return int(self.salary * self.multiplier)
    
    def calcTotalEarnings(self):
        return self.calc_salary()
    
class Manager(Employee):
    title = 'Manager'
    multiplier = 1.4
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
        
    def __str__(self):
        return super().__str__() + f' working in {self.department} as a {self.title}'
    
    def calcTotalEarnings(self):
        pass
class Executive(Manager):
    title = 'Executive Manager'
    multiplier = 1.8
    def __init__(self, name, age, salary, department, bonus):
        super().__init__(name, age, salary, department)
        self.bonus = bonus
        
    def __str__(self):
        return super().__str__() + f' with a bonus of {self.calculate_bonus()}'
    
    def calculate_bonus(self):
        return int(self.bonus)
    
    def calcTotalEarnings(self):
        return super().calcTotalEarnings() + self.calculate_bonus()
    
e1 = Employee('Amy', 29, baseSalary)
print(e1)
e2 = Manager('Joel', 35, baseSalary, 'Sales')
print(e2)
e3 = Executive('Caitlin', 42, baseSalary, 'Marketing', bonusAmount*1.1)
print(e3)

employees = {
    'Kathy': Employee('Kathy', 26, baseSalary),
    'Dale': Manager('Dale', 39, baseSalary*1.3, 'Deveopment'),
    'Micheal': Executive('Micheal', 37, baseSalary*1.1, 'Account', bonusAmount*1.15)
} 
for x in employees:
    print(employees[x])
    
