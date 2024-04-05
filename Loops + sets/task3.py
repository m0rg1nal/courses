inp = input('Enter a few numbers using coma(1, 2, 3...): ')
inp_list = inp.split(', ')
num_list = [int(i) for i in inp_list]
num_set = set(num_list)

if len(num_list) == len(num_set):
    result = 'List is unique'
else:
    result = 'List is not unique'

print(result)
