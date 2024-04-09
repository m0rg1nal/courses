roles = {'admin': ['Ivan', 'Petro'],
         'maintainer': ['Dmytro'],
         'manager': ['Oleksandr'],
         'developer': ['Maria', 'Sofia']}

name = input('Name: ')
role = [key for key, value in roles.items() if name in value]

if role:
    print(f'Hello, {role[0]}')
else:
    print(f'Hello, Guest')
