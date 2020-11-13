import random, time

game_is_active = True

class player:
    def __init__(self):
        self.action = 0
        self.ammo = 0
        self.score = 0
    def set_action(self, action):
        self.action = action
    def set_ammo(self, amount):
        self.ammo = amount
    def set_score(self, amount):
        self.score = amount


PLAYER = player()
COMPUTER = player()

def print_pre_game_menu():
    get_input = (
        input(
            '1. Start game\n'
            '2. Rulebook\n'
            '3. Score\n'
            '0. Exit\n'
            'Your choice: '
        )
    )
    try:
        return int(get_input)
    except:
        pass

## prints ammo for player and computer
def print_ammo():
    time.sleep(1)
    print('-' * 15)
    print(f'Your ammo: {PLAYER.ammo}\nComputer\'s ammo: {COMPUTER.ammo}')
    print('-' * 15)
    time.sleep(1)

## Prints winning message
def print_win():
    PLAYER.set_score(PLAYER.score+1)
    time.sleep(1)
    print('-' * 15)
    print('You won the game')
    print('-' * 15)
    time.sleep(1)

## Prints losing message
def print_defeat():
    COMPUTER.set_score(COMPUTER.score+1)
    time.sleep(1)
    print('-' * 15)
    print('You lost the game')
    print('-' * 15)
    time.sleep(1)

## Prints draw message
def print_draw():
    time.sleep(1)
    print('-' * 15)
    print('The game is drawn')
    print('-' * 15)
    time.sleep(1)

"""def print_computer_action(computer_action):
    if computer_action == 1:
        print("Computer is shooting!")
    elif computer_action == 2:
        print("Computer is loading!")
    elif computer_action == 3:
        print("Computer is blocking!")"""

def print_msg(msg):
    time.sleep(1)
    print('-' * 15)
    print(msg)
    print('-' * 15)
    time.sleep(1)

def print_msg_faster(msg2):
    print('-' * 15)
    print(msg2)
    print('-' * 15)
    

## Ends loop and resets players
def end_game():
    global game_is_active
    game_is_active = False
    PLAYER.set_action(0)
    PLAYER.set_ammo(0)
    COMPUTER.set_action(0)
    COMPUTER.set_ammo(0)


#function for shooting, outcome based on computers action
def shoot():
    if COMPUTER.action == 1:
        print_msg_faster('Computer shoots')
        print("Both players shot!")
        PLAYER.set_ammo(PLAYER.ammo-1)
        COMPUTER.set_ammo(COMPUTER.ammo-1)
    elif COMPUTER.action == 2:
        print_msg_faster('Computer loads')
        print_win()
        end_game()
    elif COMPUTER.action == 3:
        print_msg_faster('Computer blocks')
        PLAYER.set_ammo(PLAYER.ammo-1)
    elif COMPUTER.action == 4:
        print_defeat()
        end_game()


#function for blocking, outcome based on computers action
def block():               
    if COMPUTER.action == 1:
        print_msg_faster('Computer shoots')
        COMPUTER.set_ammo(COMPUTER.ammo-1)
    elif COMPUTER.action == 2:
        print_msg_faster('Computer loads')
        COMPUTER.set_ammo(COMPUTER.ammo+1)
    elif COMPUTER.action == 3:
        print_msg_faster('Computer blocks')
        print("Both players blocked!")
    elif COMPUTER.action == 4:
        print_defeat()
        end_game()


def loading():
    if COMPUTER.action == 1:
        print_msg_faster('Computer shoots')
        print_defeat()
        end_game()
    elif COMPUTER.action == 2:
        print_msg_faster('Computer loads')
        print("Both players loads!")
        COMPUTER.set_ammo(COMPUTER.ammo+1)
        PLAYER.set_ammo(PLAYER.ammo+1)
    elif COMPUTER.action == 3:
        print_msg_faster('Computer blocks')
        PLAYER.set_ammo(PLAYER.ammo+1)
    elif COMPUTER.action == 4:
        print_defeat()
        end_game()

## function for shotgunning
def shotgun():
    if COMPUTER.action == 1:
        print_msg_faster('Computer shoots')
        print("Shotgun beats regular shot!")
        print_win() 
    elif COMPUTER.action == 2:
        print_msg_faster('Computer loads')
        print_win()
    elif COMPUTER.action == 3:
        print_msg_faster('Computer blocks')
        print_win()
    elif COMPUTER.action == 4:
        print_draw()
    end_game() 


## determines computer's action
def computer_logic():
    if COMPUTER.ammo == 0:
        if PLAYER.ammo == 0:
            computer_action = 2
        else:
            computer_action = random.randint(2, 3)
    elif COMPUTER.ammo >= 3:
        computer_action = 4
    else:
        if PLAYER.ammo == 0:
            computer_action = random.randint(1, 2)
        else:
            computer_action = random.randint(1, 3)
    return computer_action


## prints menu, takes input and sets objects' actions
def print_menu():
    menu_items = ['Shoot', 'Load', 'Block', 'Shotgun']
    if PLAYER.ammo < 3:
        menu_items.remove('Shotgun')
    for i, v in enumerate(menu_items):
        print(f'{i+1}. {v}')
    print('0. Exit')
    choice = input('Enter number: ')
    try:
        PLAYER.set_action(int(choice)) ## sets player action
        COMPUTER.set_action(computer_logic()) ## sets computer action
        if PLAYER.action == 1:
            if PLAYER.ammo >= 1:
                print_msg('Shooting..')
                shoot()
                print_ammo()
                ## Shoot function
            else:
                print_msg('You need 1 or more bullets to shoot')
        elif PLAYER.action == 2:
            print_msg('Loading..')
            loading()
            print_ammo()
            ## Load function
        elif PLAYER.action == 3:
            print_msg('Blocking..')
            block()
            print_ammo()
            ## Block function
        elif PLAYER.action == 4 and PLAYER.ammo >= 3:
            print_msg('Shotgun..')
            shotgun()
            print_ammo()
        elif PLAYER.action == 0:
            ## Exits game
            end_game()
        else:
            print_msg('Pick a number between 0-3')
    except:
        print_msg('Pick a number between 0-3')

def run_game():
    while game_is_active:
        print_menu()

while True:
    choice = print_pre_game_menu()
    if choice == 1:
        run_game()
    elif choice == 2:
        print_msg(
            '1. If one shoots whilst the other loads, the shooter wins\n'
            '2. osv..'
        )
    elif choice == 3:
        print(f'Your score: {PLAYER.score}\nComputer\'s score: {COMPUTER.score}')
    elif choice == 0:
        print_msg('Exits game..')
        exit()
    else:
        print('Pick a number between 0-3')
