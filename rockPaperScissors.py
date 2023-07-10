import random
while True:
    choices = ["rock", "paper", "scissors"]

    bot = random.choice(choices)

    player = None
    while player  not in choices:
        player = input("rock, paper, or scissors: ").lower()


    if player == bot:
        print("bot: " + bot)
        print("player: " + player)
        print("it's a tie!")

    elif player == "rock":
        if bot == "paper":
            print("bot: " + bot)
            print("player: " + player)
            print("You lost!")
        if bot == "scissors":
            print("bot: " + bot)
            print("player: " + player)
            print("you won!")


    elif player == "paper":
       if bot == "rock":
           print("bot: " + bot)
           print("player: " + player)
           print("you won!")
       if bot == "scissors":
           print("bot: " + bot)
           print("player: " + player)
           print("you lost!")
           

    elif player == "scissors":
        if bot == "rock":
            print("bot: " + bot)
            print("player: " + player)
            print("you lost!")
        if bot == "paper":
            print("bot: " + bot)
            print("player: " + player)
            print("you won!")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break






