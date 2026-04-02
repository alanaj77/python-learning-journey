from game_data import data
from art import logo, vs
import random

score = 0

def compare_followers(choice, a, b):
    if choice == 'a' and a['follower_count'] > b['follower_count']:
        return True
    elif choice == 'b' and a['follower_count'] < b['follower_count']:
        return True
    return False


def is_playing():
    global score
    flag = True

    account_b = random.choice(data)

    while flag:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(logo)
        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)

        if compare_followers(choice, account_a, account_b):
            score += 1
            print(f"You are right! Your score is {score}")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            flag = False


is_playing()