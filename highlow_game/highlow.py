from art import logo, vs
from data import data
import random
import functools


def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """formatting the data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

@functools.lru_cache(maxsize = None)
def game():
    #display art
    print(logo)
    #score
    score = 0
    #Making the game reset or repeatable 
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_continue:
        #generate a random account from the data 
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        #ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #check if user is correct
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        game.cache_clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You guessed it right! Current score: {score}")
        else:
            game_continue = False
            print(f"Ooops, that's not right. Final score: {score}")

game()