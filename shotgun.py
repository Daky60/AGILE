import random

class player:
    def __init__(self):
        self.action = 0
        self.ammo = 0
    def set_action(self, action):
        self.action = action
    def set_ammo(self, amount):
        self.ammo = amount


PLAYER = player()
COMPUTER = player()

## prints ammo for player and computer
def print_ammo():
    print(f'Your ammo: {PLAYER.ammo}\nComputer\'s ammo: {COMPUTER.ammo}')
#function for shooting, outcome based on computers action
def shoot():
    if COMPUTER.action == 1:
        PLAYER.set_ammo(-1)
        COMPUTER.set_ammo(-1)
    elif COMPUTER.action == 2:
        print("Winner winner chicken dinner")
    elif COMPUTER.action == 3:
        PLAYER.set_ammo(-1)

#function for blocking, outcome based on computers action
def block():               
    if COMPUTER.action == 1:
        COMPUTER.set_ammo(-1)
    elif COMPUTER.action == 2:
        COMPUTER.set_ammo(+1)
    elif COMPUTER.action == 3:
        print("Both players blocked")

def loading():
    if COMPUTER.action == 1:
        print("LOST LOSER")
    elif COMPUTER.action == 2:
        COMPUTER.set_ammo(+1)
        PLAYER.set_ammo(+1)
    elif COMPUTER.action == 3:
        PLAYER.set_ammo(+1)
        
## determines computer's action
def computer_logic():
    if COMPUTER.ammo == 0:
        if PLAYER.ammo == 0:
            computer_action = 2
        else:
            computer_action = random.randint(2, 3)
    else:
        if PLAYER.ammo == 0:
            computer_action = random.randint(1, 2)
        else:
            computer_action = random.randint(1, 3)
    return computer_action

## prints menu, takes input and sets objects' actions
def print_menu():
    choice = (
        input(
            '1. Shoot\n'
            '2. Load\n'
            '3. Block\n'
            '0. Exit\n'
            'Your choice: '
        )
    )
    try:
        PLAYER.set_action(int(choice)) ## sets player action
        COMPUTER.set_action(computer_logic()) ## sets computer action
        if PLAYER.action == 1:
            if PLAYER.ammo >= 1:
                print('Shooting..')
                ## Shoot function
            else:
                print('You need 1 or more bullets to shoot')
        elif PLAYER.action == 2:
            print('Loading')
          
            ## Load function
        elif PLAYER.action == 3:
            print('Blocking')
            ## BLock function
        elif PLAYER.action == 0:
            exit()
        else:
            print('Choose a number between 0-3')
    except:
        print('Choose a number between 0-3')


print_menu()
