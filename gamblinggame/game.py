import coingame
import money
import slotmachine
print("You find yourself walking back to the casino as your addiction grows ever more.")
while True:
    while True:
        if money.cgw == 0 and money.smw == 0:
            game = input("Which game would you like to play first? (coin flip, slot machine) ")
            game = game.lower()
            cg = game.count("coin flip")
            sm = game.count("slot machine")
            sm2 = game.count("slut machine")
        if money.cgw == 1 and money.smw == 0:
            game = input("Which game would you like to play second? (slot machine) ")
            game = game.lower()
            sm = game.count("slot machine")
        if money.cgw == 0 and money.smw == 1:
            game = input("Which game would you like to play second? (coin flip) ")
            game = game.lower()
            cg = game.count("coin flip")
        if cg == 1 or sm == 1:
            break
        if cg == 0 and sm == 0 and sm2 == 1:
            break
        if cg == 0 and sm == 0:
            pass
    if cg == 1:
        cg = 0
        coingame.coingame()
    if sm == 1:
        sm = 0
        slotmachine.slotmachine()
    if sm2 == 1:
        sm2 = 0
        print("Christ dana")
        slotmachine.slotmachine()
    if money.cgw == -1:
        break
    if money.smw == -1:
        break