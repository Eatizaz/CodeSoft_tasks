import random

user_score = 0
machine_score = 0

while True:
    print("~~~~~~~~~Rock Paper Scissors~~~~~~~~~")
    print("~~~~~Rock wins against scissors~~~~~ \n~~~~~Paper wins against rock~~~~~ \n~~~~~Scissors wins against paper~~~~~")
    options = ["rock", "paper", "scissors"]
    machine = random.choice(options)

    user = input("Choose from rock, paper, scissors: ")
    while user not in options:
        print("Choice is not in the list")
        user = input("Choose from rock, paper, scissors: ")


    def winner(user, machine):
        if user == machine:
            return "It's a Tie"
        elif (
                (user == "rock" and machine == "scissors") or
                (user == "paper" and machine == "rock") or
                (user == "scissors" and machine == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"


    print("User choice: ", user)
    print("Computer choice: ", machine)

    result = winner(user, machine)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        machine_score += 1

    print(f"Your score: {user_score}, Computer Score: {machine_score}")

    again = input("Do you want to play again? (yes/no): ")
    if again == 'no':
        break
