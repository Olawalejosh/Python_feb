#FOR LOOP
# python_student = ['mat','burger','ram']
# for each in python_student:
#     print('Welcome', each)

#aproach one
# student_list = []
# user = int(input('How many student are taking the test: '))

# for student in range(user):
#     stud = input(f'Name of Student {student +1}: ')
#     student_list.append(stud)
# print(student)   
    
    #list comprehension aproach
# student_list = [input(f'Name of Student {student +1}:') for student in range(user)]    
# print(student_list)
    
#    # calling each student 
# for each in student_list:
#     print(f'\n{each}, Its time to take the test.\n')
          
#    #THE TEST
#     questions = ['1. how amny sides has a triangle\na.)2 b.)3',
#                  '2. Am i a male\n a.)yes b.) no',
#                 ]
#     answers = ['b','a']   
#     score = 0
#     for question , answer in zip(questions,answers):
#         print(question)
#         user_ans =input('Answer: ').strip().lower()

#         if user_ans == answers:
#             print('correct')
#             score +=5 

#     print(f'Thanks for taking the test, your total score is {score}')  
        



#ENTRANCE
# students_db =[
#     ('Tola', 'Paid'),
#     ('Josh', 'Paid'),
#     ('Marvel', 'Not-Paid')
# ]
# staff_db = [
#     ('Damilare', '25'),
#     ('Femi', '55')
# ]
# user = input('''
#      Welcome to SQI College Of ICT

#      Kindly verify your identify
#      1. Staff
#      2. Student
#      3. Visitor                            
#      4. None                           
# option: ''').strip()
# if user == '1' or user.capitalize()== 'Staff':
#     staff_id = input('ID: ').strip()
#     staff_name = input('Name: ').strip().capitalize()

#     stfnames = []
#     stfids = []
#     for namestf, idstf in staff_db:
#         stfnames.append(namestf)
#         stfids.append(idstf)

#     if staff_name in stfnames and staff_id in stfids:
#             print('Access Granted😊')
#     else:
#             print('Access Denied😒')
            
# elif user == '2' or user.capitalize() == 'Student':
#       stud_name = input('NAME: ').strip().capitalize()

#       stname = []
#       payment_status = []

#       for stn, state in students_db:
#             stname.append(stn)
#             payment_status.append(state)
#       if stud_name in stname:
#             print(f'Welcome Aboard😉 {stud_name}.\nKindly hold, lets Verify your payment status')      

#             _index = stname.index(stud_name)
#             status = payment_status[_index]

#             if status == 'Paid':
#              print('VERIFIED💕')
#             elif status != 'Paid':
#                  print('Koshi😒')



# students_db =[
#     ('Tola', 'Female'),
#     ('Josh', 'Male'),
#     ('Marvel', 'Male')
# ]

# hello = input('your name: ').strip().capitalize()
# name = []
# gender = []
# for nam, gen in students_db:
#     name.append(nam)
#     gender.append(gen)
# print(name)
# if hello in name:
#     _index = name.index(hello)
#     status = gender[_index]
#     print(f'{status}')
  
# mail = input('Enter your mail: ').strip()
# if '@' in mail or '.' in mail:
#     print('Valid Mail')
# else:
#     print('invalid')
   

#SNEAKERS MALL
menu_list =[
   ('Air Jordan', 20_000),
   ( 'Nike', 30_100),
   ('Puma', 25_300),
   ('Dior', 50_050),
   ('Nb', 42_500)
]
order = input('''
WELCOME TO JOSH MALL\n Here is our menu;
 Air Jordan = 20,000
 Nike = 30,100
 Puma = 25,300
 Dior = 50,050
 NB  = 42,500             
Kindly place your order: ''').strip().title()
sneakers = []
prices = []

orders = []
order_prices = []

for sneak, pri in menu_list:
    sneakers.append(sneak)
    prices.append(pri)

if order in sneakers:
    _index = sneakers.index(order)
    status = prices[_index]

    orders.append(order)
    order_prices.append(status)
    print(f'{order} is {status}')

while True:

    order2 = input('What else will you like to buy?\npress * to stop ordering: ').strip().title()

    if order2 == '*':
        break
    elif order2 != '*':
        if order2 in sneakers:
            _index = sneakers.index(order2)
            status = prices[_index]

            orders.append(order2)
            order_prices.append(status)
            print(f'{order2} is {status}')
        else:
            print('Item not avaliable')

for _ord, price in zip(orders,order_prices):
    print(f'{_ord}-->{price}')   

print(f'Total: #{sum(order_prices)}\nThanks for Your Patronage😍')    

