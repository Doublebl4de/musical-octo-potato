import time
import random
import wods
import money
fingers = 10
gamount = 0
prfi = 1

def coingame():
    fingers = 10
    gamount = 0
    prfi = 1
    ft = 1
    print("You walk up to your favourite, the coin flip game.")
    time.sleep(1)
    print("Suddenly, the singular coin comes alive, you're surroundings fade to nothing.")
    time.sleep(1)
    print("The coin starts screaming, \"HAHA, YOU FOOL, WHY DID YOU COME BACK TO GAMBLE AGAIN, WITH THAT SINGLE DOLLAR IN YOUR POCKET.\"")
    time.sleep(2)
    print("\"Tell you what buddy, I'll strike you a deal, you keep gambling till you get to one million dollars, and I'll let you go free, back into the real world.\"")
    time.sleep(3)
    print("\"Lose a gamble, however, I will take one of your fingers.\"")
    while True:
        if money.money == 0:
            print("Oh looks like you ran out of money, time to eat your fingers!")
            wods.die()
            money.cgw = -1
            break
        if fingers == 0:
            print("\"Those were some tasty fingers, goodnight!\"")
            wods.die()
            money.cgw = -1
            break
        if money.money >= 1000000:
            print("\"I guess you somehow gambled your way out of my clutches.\"")
            wods.win()
            money.cgw = 1
            break
        if prfi == 1:
            print("Fingers left:", fingers)
        try:
            print("Pick how much money you would like to gamble (1-",money.money,") ",sep="",end="")
            gamount = int(input())
            prfi = 0
        except:
            gamount = 0
            prfi = 0
        finally:
            pass
        if gamount >= 1 and gamount <= money.money:
            while True:
                try:
                    flip = input("Heads or tails (shop to buy fingers): ")
                    flip = flip.lower()
                    h = flip.count("heads")
                    t = flip.count("tails")
                    s = flip.count("shop")
                    w = flip.count("heads ")
                except:
                    pass
                finally:
                    if s == 1:
                        while True:
                            try:
                                b = input("Would you like to buy a finger for 100 dollars?")
                                b = b.lower()
                                y = b.count("yes")
                                n = b.count("no")
                            except:
                                pass
                            finally:
                                if y == 1 and n == 0:
                                    if money.money > 100:
                                        print("Ok, here ya go, one fingers")
                                        print("Money - 100")
                                        money.money -= 100
                                        fingers = fingers + 1
                                        break
                                    if money.money <= 100:
                                        print("Sorry, it seems you have insufficient funds")
                                        break
                                if y == 0 and n == 1:
                                    print("Then get back to gambling you bafoon")
                                    break
                                if (y == 1 and n == 1) or (y == 0 and n == 0):
                                    pass
                    if h == 1 and t == 0:
                        break
                    if t == 1 and h == 0:
                        break
                    elif (t == 1 and h == 1) or (t == 0 and h == 0):
                        pass
                    else:
                        pass
            flipped = random.randint(1,2)
            if ft == 1:
                if h == 1:
                    flipped = 1
                if t == 1:
                    flipped = 1
                ft = 0
            if (w == 1 and flipped == 2):
                flipped = 1

            if (h == 1 and flipped == 1) or (t == 1 and flipped == 2):
                if h == 1 and flipped == 1:
                    print("Heads! Congratulations!")
                    money.money += gamount
                    print("Money + ",gamount,sep="")
                if t == 1 and flipped == 2:
                    print("Tails! Congratulations!")
                    money.money += gamount
                    print("Money + ",gamount,sep="")
            elif (h == 1 and flipped == 2) or (t == 1 and flipped == 1):
                if h == 1 and flipped == 2:
                    print("Heads. That's too bad, time to take a finger.")
                    money.money -= gamount
                    fingers -= 1
                    print("Money - ",gamount,sep="")
                if t == 1 and flipped == 1:
                    print("Tails. That's too bad, time to take a finger.")
                    money.money -= gamount
                    fingers -= 1
                    print("Money - ",gamount,sep="")
            h = 0
            t = 0
            prfi = 1