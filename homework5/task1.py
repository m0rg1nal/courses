user_inp = input("Palindrome check: ").lower()
inp_reversed = user_inp[::-1]
if inp_reversed == user_inp:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
