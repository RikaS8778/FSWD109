"""
6. **String Slicing:**

   Given a string `sentence`, extract the first five characters and print them.
"""
#Q6.
sentence = "Those things are not true"
print(sentence[:5])
 
"""
7. **List Operations:**

   Perform the following operations on a list `numbers`:

   - Append the number '10'.

   - Remove the number '5'.

   - Print the final list.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.append(10)
numbers.remove(5)
print(numbers)

"""
8. **Dictionary Operations:**

   Consider a dictionary `person` with keys 'name', 'age', and 'city'. Print all the key-value pairs using a loop.
"""
person = {'name': 'Linda', 'age': 28, 'city': 'Los Angeles'}
for key, value in person.items():
    print(f'{key}: {value}')
 
"""
9. **Boolean Evaluation:**

   Check if the variable `num` is greater than 10. If it is, print "Greater than 10"; otherwise, print "Less than or equal to 10".
"""
num = 29
if num > 10:
    print("Greater than 10")
elif num == 10:
    print("num is equal to 10")
else:
    print("Less than or equal to 10")
 
"""
10. **Function with Default Parameter:**

    Write a Python function named `greet` that takes a parameter `name` with a default value of "Guest". The function should print "Hello, [name]!" where [name] is replaced with the value passed or the default value if none is provided.
"""    
name = 'Alice'
def greet(name:str = 'Guest') -> None:
    print(f'Hello, {name}!')
    
greet(name)
greet()