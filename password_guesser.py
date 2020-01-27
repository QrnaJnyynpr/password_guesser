import random, string, time
from random import randint

characters = string.punctuation + string.ascii_uppercase + string.ascii_lowercase
character_list = [character for character in characters]

while True:
	password = input("\nPlease enter a password to test:\n")

	start_timer = time.time()
	print("\nWorking...\n")

	def brute_force():
		guess = ""
		guess_count = 0
		password_length = len(password) + 1

		while guess != password:
			guess = "".join(list((random.choice(character_list) for num in range(randint(1,password_length)))))
			# print(f"> {guess}")
			guess_count += 1

		print(f"\nYour password is: {guess}")
		print(f"Attempts taken: {guess_count}")
		timer()

	def timer():
		end_timer = time.time()
		total_time = end_timer - start_timer
		print(f"Time taken to guess: {round(total_time, 4)} seconds")

	with open('password_dictionary.txt') as password_dictionary:
		if "\n" + password + "\n" in password_dictionary.read():
			print(f"Your password is: {password}")
			timer()
		else:
			print("Dictionary attack failed.\nAttempting brute force...")
			print("This might take some time.")
			brute_force()