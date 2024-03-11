# # name = 'JOSH has a gun. He loves food '
# # print(name.capitalize())
# # print(name.upper())
# # print(name.lower())
# # name = 'JOSH has a ' + 'gun'.capitalize()
# # print(name)
# # print(name.strip())
# # print(name.split())
# # word_split = name. split()
# # word_join = ' '.join(word_split)
# # print(word_join)

# # mail = input('Enter email').strip()
# # if mail.find('@') == 'jjj':
# #  print('valid email')


#     #ESCAPE CHACRACTERS
# #\t is for tab
# #\b is for backspace
# #\n is enter
# #\r is return

# # expression = r'this is the path to my python file - C:\python_feb\new_file\read_python\think_python'

# #PYTHON COLLECTIONS
# '''
# 1.LIST [] or list()
# properties of a list
# i) Ordered
# ii) Changeable/mutable
# iii) It allows duplicate values
# iv) It can be indexed
# '''
# my_list = ['Ola', 'Josh', 'Bottle', 45, True, ['Yam' ,'Rice', 'Semo'],'Bottle']
# # print(my_list[5][1]) 
 
# #slicing
# # print(my_list[2:])
# # my_list[0] = 'Mary'
# # my_list[0:3] = 'Tolu', 'mary'.capitalize(), 'Dave'
# # print(my_list)


# #FUNCTIONS
# # APPEND
# li =[]
# # li.append(['cat', 'brain'])
# # print(li)
# #EXTEND
# # li.extend(['cat', 'brain'])
# # print(li)
# # my_list.clear()
# # del my_list
# # my_list.pop(4)
# # my_list.remove('Bottle')
# # my_list.reverse()
# # print(my_list.count('Bottle'))
# # print(my_list.index('Bottle'))
# # print(my_list.insert(0, 'Josh'))

# #TUPLE
# student = ('pig', 'ram' , 'rat', 'teeth')
# list_of_student = list(student)
# # print(list_of_student)
# #unpacking
# *list_of_student, = student
# (student1, student2, *alls) = student
# # print(student1, *student2, alls)

# scores = [20, 35, 65, 70]
# # print(max(scores))
# # index_max =scores.index(max(scores))
# # print(student[index_max])
    

# for name, score in zip(student, scores):
#     # print(f'{name} scored {score}')
 

# #  questions = [('1. how amny sides has a triangle a.)2 b.)3', 'b')]
# # [( '2. Am i a male a.)yes b.) no', 'a')]
                
# # score = 0
# # for quest, ans in questions:
# #  print(quest)
# #  user = input('Answer: ').strip().lower()
# #  if user == ans:
# #   print('correct')
# #   score += 5
# #  else:
# #   print('wrong')

# # print(f'your total score is  {score}')  

# #WHILE LOOP
#     #  slot = 10 
#     #  admission_list = []

#     #  while slot >= 1:
#     #       name = input('aspirant name: ')
#     #       admission_list.append(name)
          
#           #SET
#     # myset = {'apple' 'mango' 'pineapple'}
#     # myset.add()
#     # myset.update()
#     # fruit = myset.copy()
#     # myset.pop()
#     # myset.remove()



    #DICTIONARY
# car = {'Model': 'Tesla', 'Year': 2022}
# print('The model is', car['Model'])

# quiz = {
#     '1. how many side has a triangle?': 3,
#     '2. Lagos is a__': 'State'
# }
# for quest, ans in quiz.items():
#     print(quest)
#     user = input('Answer the questions below: ')
#     if user ==ans:
#       print('sure')

{'Student1':{'name': 'Josh', 'Matno': '195613'},
'Student2':{'name': 'Marvel', 'Matno': '190001'}
 }
user = input('Kindly press 1 to start registration: ')
if user == '1':
    x = 1
    student_db ={}

    while True:
        name = input('Name: ').strip().title()
        matno= input('Matno: ').strip().title()

        students = {'name': name, 'matno': matno}
        student_db.update({f'student{x}':students})
        x += 1

        user = input('press 2 to stop or Enter to continue: ')
        if user == '2':
            break

print(student_db)        