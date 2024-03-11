class Calculator:
    def __init__(self):
        self.calc_name = 'Casio'

        self.home()

    def home(self):
        print(f'Welcome to {self.calc_name}') 
        self.value1 = float(input('First value: '))
        self.value2 = float(input('Second value: '))

        user = input('''
                    Select an operation to perform
                    1. Addition
                    2.Subtraction
                    3.Division
                    4.Multiplicatiom
                    *.Exit
                    option: ''')

        if user == '1':
             self.addition()

        elif user == '2':
               self.subtraction()
 
        elif user == '3':
            self.division()
        elif user == '4':
            self.multiplication()
        elif user == '*':
          exit()
        else:
         print('Invalid command')
        self.home()


    def addition(self):
       print(f'Ansswer = {self.value1 + self.value2}')
       self.decide()

    def subtraction(self):
       print(f'Ansswer = {self.value1 - self.value2}')
       self.decide()

    def division(self):
       print(f'Ansswer = {self.value1 / self.value2}')
       self.decide()

    def multiplication(self):
       print(f'Ansswer = {self.value1 * self.value2}')
       self.decide()

    def decide(self):
        user = input('Press 1 to go home or # to exit: ')  
        if user == '1':
            self.home()
        else:
            exit() 
       
casio = Calculator()









