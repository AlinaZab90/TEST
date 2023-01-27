import random

variants = ['rock', 'paper', 'scissors', 'lizard', 'spock']
wins = 0
loses = 0
draws = 0


while True:
    your_hand = input("Enter your choice: ")
    if your_hand not in variants:
        print("Your choise is unacceptable")
        continue
    
    computer_hand = random.choice(variants)
    print("Your hand: ", your_hand)
    print("Computer hand: ", computer_hand)


    if your_hand == computer_hand:
        print("It's a drawt")
        draws +=1

    elif your_hand == 'rock':
        if computer_hand == 'paper':
            loses += 1
            print("You lost")
        else:
            wins += 1
            print("You won")

    elif your_hand == 'papper':
        if computer_hand == 'scissors':
            loses += 1
            print("You lost")
        else:
            wins += 1
            print("You won")

    elif your_hand == 'scissors':
        if computer_hand == 'rock':
            loses += 1
            print("You lost")
        else:
            wins += 1
            print("You won")

    elif your_hand == 'paper':
        if computer_hand == 'rock':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")

    elif your_hand == 'spock':
        if computer_hand == 'paper':
            print("You lost")
        else:
            print("You won")

    elif your_hand == 'spock':
        if computer_hand == "paper":
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")

    elif your_hand == 'spock':
        if computer_hand == 'rock':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")

    elif your_hand == 'spock':
        if computer_hand == 'scissors':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")
    
    elif your_hand == 'spock':
        if computer_hand == 'lizard':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")
    
    elif your_hand == 'lizard':
        if computer_hand == 'rock':
            loses += 1
            print("You lost")
        else:
            wins += 1
            print("You won")
    elif your_hand == 'lizard':
        if computer_hand == 'paper':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")

    elif your_hand == 'scissors':
        if computer_hand == 'lizard':
            wins += 1
            print("You won")
        else:
            loses += 1
            print("You lost")


    print("wins: ", wins, "loses: ", loses, "draws: ", draws)
