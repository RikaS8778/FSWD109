"""
11. **String Interpolation:**

    Create a Python function named `format_string` that takes two parameters `name` and `age`. Use string interpolation to return a formatted string like "My name is [name] and I am [age] years old."
"""
#Q11,
def format_string(name, age):
    return('My name is {name} and I am {age} years old.' .format(name=name, age=age))

print(format_string('Amy', 28))

"""
12. **Dictionary Manipulation:**

    Write a Python code to remove the key-value pair where the key is 'age' from a dictionary `person`.
"""
person = {'name': 'Joe', 'age': 30, 'city': 'New York'}
if 'age' in person:
    person.pop('age')
    print(person)
    
"""
13. **Conditional with List:**

    Given a list of numbers `numbers`, iterate through each number and print "Even" if it's even, and "Odd" if it's odd.
"""
#Q13,
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if(number%2 == 0):
        print(f'{number} is Even')
    else:
        print(f'{number} is Odd')
 
"""
14. **Loop with String:**

    Write a Python program that takes a string `word` as input and prints each character of the string along with its index.
"""
#Q14,
word = 'Python'

def print_word_with_index(word: str):
    length = len(word)
    for i in range(length):
        print(f'Index: {i}, Character: {word[i]}')

print_word_with_index(word)


"""
15. **Function with Variable Arguments:**

    Define a Python function named `average` that takes a variable number of arguments and returns the average of all the arguments passed.
"""
def average(numbers: list) -> float:
    
    return sum(numbers) / len(numbers)

numbers = [88, 78, 100, 56, 69, 92]

print(average(numbers))

from statistics import mean
avr = mean(numbers)
print(avr)
print(round(avr))