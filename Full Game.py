import random

def get_computers_choice():
    options = ['rock', 'paper', 'scissors']
    computers_choice = random.choice(options)
    return computers_choice

def get_user_input():
    while True:
        user_input = input('Enter rock/paper/scissors: ').lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input

def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return 'draw'
    elif (user_pick == 'paper' and computer_pick == 'rock') or (user_pick == 'rock' and computer_pick == 'scissors') or (user_pick == 'scissors' and computer_pick == 'paper'):
        return 'win'
    else:
        return 'lose'

computer_pick = get_computers_choice()
users_pick = get_user_input()
result = get_result(users_pick, computer_pick)

print(f"Computer's pick: {computer_pick}")
print(f"Your pick: {users_pick}")
print(f"You {result}")
