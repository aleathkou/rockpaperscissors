import random
player_wins = 0
cpu_wins = 0
wlratio = 0
options =  ["rock", "paper", "scissors"]


while True:
		user_input = input("TYPE rock, paper, OR scissors, q TO EXIT: ").lower()
		if user_input == "q":
			break
			
		
		if user_input not in ["rock", "paper", "scissors"]:
			continue
		
		random_number = random.randint(0, 2)
		
		computer_pick = options[random_number];
		print("COMPUTER PICKED", computer_pick + ".")
		
		if user_input == "rock" and computer_pick == "scissors":
			player_wins += 1
			print("You won!")
			
				
		elif user_input == "scissors" and computer_pick == "paper":
			player_wins += 1
			print("You won!")
			
		elif user_input == "paper" and computer_pick == "rock":
			player_wins += 1
			print("You won!")
			
		else: 
					if user_input == computer_pick:
						print("IT'S A TIE!")
					else:
						print("CPU WINS!")
						cpu_wins+=1


print("THANKS FOR PLAYING, YOU WON", player_wins, "TIMES")
print( "CPU WON", cpu_wins, "TIMES")
wlratio = player_wins / (player_wins + cpu_wins)
print("WIN TO LOSE RATIO OF", wlratio)