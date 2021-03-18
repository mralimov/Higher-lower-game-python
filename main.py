from art import logo, vs
from game_data import data
import random
from replit import clear

loose = False
score = 0
print(logo)
while not loose:
    nominate_a = random.choice(data)
    nominate_b = random.choice(data)
    if nominate_a == nominate_b:
        nominate_b = random.choice(data)

    def call_nominate(data_nominate):
        return f' {data_nominate["name"]}, a {data_nominate["description"]}, from {data_nominate["country"]}.'

    def calc_nominates(nom_a, nom_b):
        if nom_a > nom_b:
            nom_a = "a"
            return nom_a
        else:
            nom_b = "b"
            return nom_b

    a_follower_count = nominate_a["follower_count"]
    b_follower_count = nominate_b["follower_count"]

    print(f"Compare A: {call_nominate(nominate_a)}.")

    print(vs)

    print(f"Compare B: {call_nominate(nominate_b)}.")
    ask_choice = input("Who has more followers? Type 'A' or 'B':  ").lower()
    if ask_choice == calc_nominates(a_follower_count, b_follower_count):
        score += 1
        clear()
        print(logo)
        print(f"You got it right! Current score. {score}")

    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        loose = True
