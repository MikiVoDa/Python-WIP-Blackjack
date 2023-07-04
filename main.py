import random
import time
from os import system, name
def cls():
    if name == 'nt':
        _ = system('cls')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True
def hit_me():
    carte = random.choice(cards)
    return carte
while play_again == True:
    end_game = False
    suma_tu = 0
    suma_pc = 0
    carti_tu = []
    carti_pc = []
    carte_tu = hit_me()
    carte_pc = hit_me()
    suma_tu += carte_tu
    suma_pc += carte_pc
    carti_tu.append(carte_tu)
    carti_pc.append(carte_pc)
    carti_pc[0] = "*"
    carte_tu = hit_me()
    carti_tu.append(carte_tu)
    suma_tu += carte_tu
    carte_pc = hit_me()
    carti_pc.append(carte_pc)
    suma_pc += carte_pc

    while end_game == False:
        print("Se impart cartile...\n")
        time.sleep(0.5)
        cls()
        print(f"You have {carti_tu}.\nTotal is {suma_tu}.\nThe dealer has {carti_pc}.")
        hit = input("Hit or Stay? h/s\n")
        if hit == "h":
            carte_tu = hit_me()
            print(f"You got a {carte_tu}.")
            if carte_tu == 11 and suma_tu + carte_tu > 21:
                carte_tu = 1
                print("The ace has turned into 1.")
            carti_tu.append(carte_tu)
            suma_tu += carte_tu
            if suma_tu == 21:
                print("Blackjack!")
                break
            if suma_tu > 21:
                time.sleep(1)
                print("Bust")
                break
            if suma_pc < 17:
                carte_pc = hit_me()
                print(f"Dealer got a {carte_pc}.")
                print(f"The dealer has {carti_pc}.")
                carti_pc.append(carte_pc)
                suma_pc += carte_pc
                break

        else:
            while hit == "s":
                if suma_pc < 17:
                    carte_pc = hit_me()
                    print(f"Dealer got a {carte_pc}.")
                    print(f"The dealer has {carti_pc}.")
                    carti_pc.append(carte_pc)
                    suma_pc += carte_pc
                else:
                    if suma_tu == 21:
                        print(f"Dealer got a {carte_pc}.")
                        print(f"The dealer has {carti_pc}.")
                        time.sleep(1)
                        print("You Win!")
                        break
                    elif suma_pc > 21:
                        print(f"Dealer got a {carte_pc}.")
                        print(f"The dealer has {carti_pc}.")
                        time.sleep(1)
                        print("You Win!")
                        break
                    elif suma_pc > suma_tu:
                        print(f"Dealer got a {carte_pc}.")
                        print(f"The dealer has {carti_pc}.")
                        print("Dealer wins!")
                        break
                    elif suma_pc < suma_tu:
                        print(f"Dealer got a {carte_pc}.")
                        print(f"The dealer has {carti_pc}.")
                        time.sleep(1)
                        print("You Win!")
                        break
                    else:
                        print(f"Dealer got a {carte_pc}.")
                        print(f"The dealer has {carti_pc}.")
                        print("Its a Draw!")
                        break
            break
    y_n = input("Play again? y/n\n")
    if y_n == "n":
        play_again = False
