import random

 
user_score = 0
computer_score = 0

print("""
🎮 Welcome to the Rock-Paper-Scissors Game! 🎮
Rules:
- 🪨 Rock beats ✂️ Scissors
- ✂️ Scissors beat 📄 Paper
- 📄 Paper beats 🪨 Rock

How to Play:
- Type "rock," "paper," or "scissors" to make your choice.
- Type "quit" to exit the game.

Let's begin!
""")

while True:
    
    user_choice = input("Your choice (rock/paper/scissors): ").lower()
    if user_choice == "quit":
        print("Thanks for playing! See you next time!")
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue

  
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
 
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😢 Computer wins this round!")
        computer_score += 1

 
    print(f"\nCurrent Scores:\nYou: {user_score} | Computer: {computer_score}\n")
 
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        print(f"Final Scores: You: {user_score} | Computer: {computer_score}")
        break
