# print('My name is Joshua')
# print('My name ' + 'is Joshua')
 
# first_name = 'Joshua'
# last_name = 'Olawale'
# age = 12
# height = 2.5

# print('My name is', first_name)
#print('My name is ' + first_name  +' ' +last_name + ' ' 'I am' , age , 'I am' , height)
#print(f'My name is {first_name} {last_name},I am {age} years old') 
a = 7
b = 3
# print(f'{a} + {b} = {a + b}')
# print( str(a) + ' + ' + str(b) + ' = ' + str(a+b) )
val1 = bin(20)
val2 = bin(40)

# print(f'{val1} | {val2} = {bin(40 | 20)}')
# print(f'{val1} ^ {val2} = {bin(40 ^ 20)}')
# print(bin(~40))
# print(bin(40>>2))
# x = 7
# if x == 5:
#     print(f'{x} is equal to 5')
# else:
#     print(f'{x} is not equal to 5')


# user = input('USSD code').strip()
# if user == '*312#':
#     print('''
# 1. Data Plan
# 2. Check Balance
# 3. Social Bundle  
# 4. Borrow Credit                  
# ''')
#     user = input('choice: ')
#     if user == '1':
#         print('''DATA PLAN
#               1.daily plan
#               2.weekly plan
#               3.monthly plan
#               ''')
#     elif user == '2':
#         print('CHECK BALANCE')
#     elif user == '3':
#         print('''
#               1.Whatsapp
#               2.Facebook
#               3.Instagram
#               ''')
#     elif user == '4':
#         print('''
#               1.Borrow Airtime
#               2.Borrow Data
#               3.Recharge
#               ''')
#     else:
#         print('Ivalid command')


# else:
#     print('Invalid Ussd Code')

# user = input('autorenew, yes or no? ').lower().strip()
# if user == 'yes':
#      print('Autorenew successful')
# # elif user == 'Yes':
# #     print('Autorenew successful')
# # elif user == 'YES':
# #     print('Autorenew successful')
# else:
#  print('Autorenew decline')



class ussd:
    def __init__(self) -> None:
        self.name = 'MTN'

        self.home()

    def home(self):
        print(f'Yellow, Welcome to My{self.name} services')  
        user = input('USSD CODE: ').strip()
        if user != '*312#':
            print('invalid code')
        else:
            choice =  input('''
                             1. Data Plan
                             2. Check Balance
                             3. Social Bundle  
                             4. Borrow Credit                  
                       Option: ''').strip().title()
            
        if choice == '1':
            self.dataplan()
            self.decide()

        elif choice == '2':
            self.balance() 
            self.decide()

        elif choice == '3':
            self.bundle()
            self.decide()

        elif choice == '4':
            self.borrow()
            self.decide()


    def dataplan(self): 
         print('''DATA PLAN
              1.daily plan
              2.weekly plan
              3.monthly plan
              ''') 
    def balance(self):             
             print('CHECK BALANCE')
    def bundle():
        print('''
              1.Whatsapp
              2.Facebook
              3.Instagram
              ''')
    def borrow():
        print('''
              1.Borrow Airtime
              2.Borrow Data
              3.Recharge
              ''')
        
    def decide(self):
        user = input('Press 1 to go home or # to exit: ')  
        if user == '1':
            self.home()
        else:
            exit() 

            
mtn = ussd()
         