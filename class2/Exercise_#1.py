"""
    1. **Multiple Variable Assignment:**

    Write a Python code to assign values '1', '4', and '3' to variables `a`, `b`, and `c` respectively in a single line.
"""
#Q1. 
a, b, c = 1, 4, 3
print(a, b, c)
    
"""
    2. **String Length:**

    Create a Python program to find the length of a given string `text` and print it.
"""
#Q2.
text = "text"
print(len(text))

"""
    3. **List Manipulation:**

    Write a Python script to add an element 'apple' to the end of a list `fruits`.

"""
#Q3.
fruits = ['banana', 'orange', 'mango']
fruits.append('apple')
print(fruits)

"""
    4  . **Dictionary Length:**

   Write a Python code to find the number of key-value pairs in a dictionary `my_dict`.
"""

#Q4.
my_dict = {'name': 'Josh', 'age': 35, 'job': 'software engineer', 'married': False}
count  = len(my_dict)
print(count)
print(my_dict.items())

"""
5. **Global vs Local Variables:**

   Define a global variable `x` outside a function and a local variable `x` inside a function. Print both variables to observe the scope difference.

"""
x = 100
a = 2
mult = a*x
print(f'{mult} #x is the global variable')

def newFunction(a: int, ) -> int:
    x = 10
    return a*x

print(f'{newFunction(a)} #x is the global variable')

