x = 15
if x > 20:
    print('A')
elif x > 10:
    print('B')
else:
    print('C')

age = 17
has_id = True
if age >= 18 and has_id:
    print('Allowed')
else:
    print('Denied')

def calculate(a, b):
    return a + b

print(calculate(5, 3))


def greet(name='Student'):
    print('Hello', name)

greet()

def check_number(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(check_number(7))