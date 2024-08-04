from art import logo, vs
from game_data import data
import random
import os

def get_person():
    """Gets a random value from the data list in game_data and erases it from data list"""
    follow_account = data[random.randint(0, len(data)-1 )]
    data.remove(follow_account)
    return follow_account

value_A = get_person()

guess_right = True

Score = 0

while guess_right == True and len(data) != 0:
    
    print(logo)
    
    if Score > 0:
        print(f"You are right! Current score: {Score}")
    
    print(f"Compare A: {value_A['name']}, a {value_A['description']}, from {value_A['country']}.")
    A_followers = value_A['follower_count']
    
    print(vs)
    
    value_B = get_person()
    
    print(f"Against B: {value_B['name']}, a {value_B['description']}, from {value_B['country']}.")
    B_followers = value_B['follower_count']
    
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if user_input == 'a':
        com_value = A_followers > B_followers
    else:
        com_value = B_followers > A_followers
        
    if com_value == True:
        Score += 1
        value_A = value_B
    else:
        guess_right = False
        
    os.system('cls')

print(logo)

if len(data) == 0:
    print(f"\nWe have run out of data. You have won the game! Final Score: {Score}")
else:      
    print(f"\nSorry that's wrong. Final score: {Score}\n")