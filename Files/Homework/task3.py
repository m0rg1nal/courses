course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

key = input('Enter a key to the dictionary: ').lower()

try:
    print(course[key])
except KeyError:
    print('There is no such key in the dictionary')
