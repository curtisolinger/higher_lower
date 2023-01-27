import random
import sys
import os
from art import logo, vs
from game_data import data


def main():
	choice0 = random.choice(data)
	choice1 = random.choice(data)
	continue_playing = True
	score = 0

	while continue_playing:
		os.system('clear')
		print(logo)

		if score > 0:
			print(f"You are right! Current score: {score}")

		print(f"Compare A: {choice0['name']}, a {choice0['description']}, from {choice0['country']}.")
		print(vs)
		print(f"Against B: {choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
		
		while True:
			response = input("Who has more followers? Type 'A' or 'B': ").upper()
			if response in ['A', 'B']:
				break
			else:
				print("Invalid input")


		right_answer = who_has_more_followers(x = choice0, y = choice1)

		if response == right_answer:
			score += 1
			choice0 = choice1
			choice1 = random.choice(data)

			while choice0 == choice1:
				choice1 = random.choice(data)			

		else:
			print(f"Sorry, that's wrong. Final score {score}")
			continue_playing = False


def who_has_more_followers(x, y):
	if x['follower_count'] >= y['follower_count']:
		return "A"
	else:
		return "B"


main()