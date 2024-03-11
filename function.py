# val1 = "josh"

# def no_me():
#     gender = 'male'
#     print(f'my name is {val1}. i am a {gender} child')
# no_me()   


def landing_page():
    global val1
    global val2
    val1 = float(input('Value1: '))
    val2 = float(input('Value2: '))
    name = input('Your name: ')

    user = input(f''' Welcome to my Alata {name}
     1. Addition
     2. Subtraction
     #. Exit              
Choose your option: ''').strip()
    if user == '1':
        addition()
    elif user == '2':
        subtraction()
    elif user == '#':
        exit()
    else:
        print('Invalid')
        landing_page()


def addition():
    print(f'Ans: {val1 + val2}')
    decide()        
    

def subtraction():
    print(f'Ans: {val1 - val2}')
    decide() 


def decide():
    user = input('press 1 to go to home or # to exit: ').strip()
    if user == '1':
        landing_page()
    else:
        exit()   
    


# landing_page()






# def add(val1: float, val2: float = 10):
#     '''
#     I added things up
#     '''
#     return val1 + val2


# def arithmetic():
#     res = 2 ** add(10)
#     return res

# def printf(name):
#     print(f'{name}, Your Result is {arithmetic()}')

# printf(input('Your Name: '))    
    



# class Dust:
#     def __init__(self):
#          self.first_name = 'Josh'
#          self.last_name ='Olawale'
#          age = ''

#     def naming(self):
#         print(f'My name is {self.first_name} {self.last_name}')


# father = Dust()
# father.naming()




#INHERITANCE
# class parent:
#     def __init__(self) -> None:
#         self.surname = 'Ojo'
#         self.firstname = 'Mary'
#         self.hobby = 'Eating'

#         self.describe()

#     def describe(self):
#         print(f'My name is {self.firstname} {self.surname}, I love {self.hobby}')

# class Child(parent):
#     def __init__(self) -> None:
#         super().__init__()            




#BANK
class Bank:
    def __init__(self) -> None:
        self.bankname = 'UBA'
        self.rc_no = '84564858'
        self.branch = 'Abuja'

    def home(self):
        print(f'''
Welcome to {self.bankname} {self.rc_no}, {self.branch}
1. Sign up
2. Sign in
''')

bank = Bank()

class NewBranch(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.branch ='Ogbomosho'

new = NewBranch()
# new.home()        