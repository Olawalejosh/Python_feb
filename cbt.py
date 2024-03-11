# print('RAIN SEMESTER EXAMINATION')
# print('''
#       MTH 101
#       1. 2. 3. 4. 5.
#       ''')
# student = input('start: ').strip()
# if student == '1':
#     print('''The product of 6 and 2 is __ 
#           A:14
#           B:12
#           C:9
#           D:11
#           ''')
# candidate = input('provide answer ').lower().strip()
# if candidate == 'b':
#         print('CORRECT')
# else:
#       print('wrong')

# if student == '2':
#     print(''' 140 / 2 is __ 
#           A:123
#           B:45
#           C:71
#           D:70
#           ''')
# candidate = input('provide answer ').strip().lower()
# if candidate == 'd':
#         print('CORRECT')
# else:
#       print('wrong')
name = input('Your Name: ')
user = input('Press Enter to start or 1 to exit: ')
score = 0
print('The product of 6 and 2 is__\n)13 b.)12 .c)9 .d)14')
user = input('Answer: ').strip().capitalize()
if user == 'D':
    print('CORRECT')
    score += 5
else:
    print('wrong')

    print(f'Thanks for taking the test{name}, your total score is{score}')