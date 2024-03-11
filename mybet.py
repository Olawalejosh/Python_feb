myset = {'apple' 'mango' 'pineapple' 'cherry'
         'strawberry' 'guava' }
deposit = float(input('Kndly deposit here: '))
balance = deposit
stake = float(input('Stake: '))

while balance > 0 and balance > stake:
    guess = input('Guess the fruit: ').strip().lower()
    choosen_fruit = myset.pop()
    myset.add(choosen_fruit)

    if guess == choosen_fruit:
        balance += 5* stake
        print(f'YOU WON\nYour balance is {balance}')

    else:
        balance -= stake
        print(f'LOST😂\nYour balance is {balance}')


        user = input('press # to exit: ')
        if user ==' #':
         break
else:
           print('Insufficient Funds😒')





class Bet:
    def __init__(self) -> None:
          self.bet_name = 'Josh Bet'

          self.home()


    def home(self):
        print(f'Welcome to {self.bet_name}')
        self.myset = {'apple' 'mango' 'pineapple' 'cherry'
        'strawberry' 'guava' }
        self.deposit = float(input('Kndly deposit here: '))
        self.balance = self.deposit

        self.dashboard()

    def dashbaord(self):
        print(f'Your current balance is {self.balance}')
        
        self.stake = float(input('Stake: '))
        user = ('Press 1 to play')
        if user == '1': 
             self.game()


    def game(self):
         
        while self.balance > 0 and self.balance > self.stake:
            guess = input('Guess the fruit: ').strip().lower()
            choosen_fruit = myset.pop()
            myset.add(choosen_fruit)

            if guess == choosen_fruit:
                balance += 5* stake
                print(f'YOU WON\nYour balance is {balance}')

            else:
                balance -= stake
                print(f'LOST😂\nYour balance is {balance}')


                user = input('press # to exit: ')
                if user ==' #':
                    break
        else:
            print('Insufficient Funds😒')


bet = Bet()




             