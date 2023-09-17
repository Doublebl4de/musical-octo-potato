import time
import random
import wods
import money
hairs = 100
prha = 1
def slotmachine():
    hairs = 100
    prha = 1
    ft = 1
    print("You walk up to your second favourite, the slot machine.")
    time.sleep(1)
    print("Suddenly, the slot machine comes to life, you're surroundings fade to nothing.")
    time.sleep(1)
    print("The machine starts whirring, producing a robotic voice, \"B A C K  T O  G A M B L E  I  S E E\"")
    time.sleep(1)
    print("\"R E C E N T L Y  I  H A V E  D E V E L O P E D  A  L I K I N G  T O  E A T I N G  H U M A N  S C A L P S\"")
    time.sleep(1)
    print("\"B U T  P E S K Y  H A I R  A L W A Y S  G E T ' S  I N  T H E  W A Y\"")
    time.sleep(1)
    print("\"I  W I L L  T A K E  Y O U R  H A I R S  B A S E D  O N  H O W  F A R  T H E  G R E A T E S T  N U M B E R  I S  A W A Y  F R O M  T H E  S M A L L E S T\"")
    time.sleep(1)
    print("\"I F  Y O U  G E T  A  M A T C H  I  W I L L  L E T  Y O U  G O  A N D  N O T  E A T  Y O U R  S C A L P\"")
    time.sleep(1)
    print("\"T H E  C O S T  T O  P L A Y  I S  O N E  D O L L A R S ,  S P E C I F I C  M A T C H S  W I L L  G A I N  Y O U  M O N E Y  B U T  N O T  S A V E  Y O U R  H A I R S\"")
    while True:
        if money.money == 0:
            print("I T  S E E M S  Y O U  H A V E  R U N  O U T  O F  M O N E Y ,  Y U M  Y U M  H U M A N  S C A L P  T I M E")
            wods.die()
            money.smw = -1
            break
        if hairs == 0:
            print("E X P O S E D  S C A L P ! ! !  Y U M  Y U M  H U M A N  S C A L P  T I M E")
            wods.die()
            money.smw = -1
            break
        if prha == 1:
            print("Hairs left:", hairs)
            print("Money:",money.money)
        try:
            yon = input("Would you like to spend one dollars to use the slot machine? (shop to buy hairs) ")
            yon = yon.lower()
            yony = yon.count("yes")
            yonn = yon.count("no")
            s = yon.count("shop")
            w = yon.count("yes ")
        except:
            prha = 0
        finally:
            pass
        if s == 1:
            while True:
                try:
                    bu = input("H A I R  F O R  1 0  D O L L A R S ? ")
                    bu = bu.lower()
                    y = bu.count("yes")
                    n = bu.count("no")
                    infinite = bu.count("infinite hairs please")
                except:
                    pass
                finally:
                    if y == 1 and n == 0:
                        if money.money > 10:
                            print("O N E  H A I R  C O M I N G  U P")
                            print("Money - 10")
                            money.money -= 10
                            break
                        if money.money <= 10:
                            print("Y O U  A R E  P O O R")
                            break
                    if y == 0 and n == 1:
                        print("N O  E S C A P E")
                        break
                    if (y == 0 and n == 0) and infinite == 1:
                        hairs = 100000000000000000000000000000000000
                        print("C H E A T E R")
                        break
                    if (y == 1 and n == 1) or (y == 0 and n == 0):
                        pass
        if yonn == 1 and yony == 0:
            print("Y O U  C A N ' T  E S C A P E")
            pass
        elif (yonn == 1 and yony == 1) or (yonn == 0 and yony == 0):
            pass
        else:
            pass
        if yony == 1 and yonn == 0:
            print("Money - 1")
            money.money -= 1
            for i in range(10):
                a = random.randint(1,9)
                b = random.randint(1,9)
                c = random.randint(1,9)
                print(a,b,c)
                time.sleep(0.1)
            for i in range(5):
                a = random.randint(1,9)
                b = random.randint(1,9)
                c = random.randint(1,9)
                print(a,b,c)
                time.sleep(0.5)
            for i in range(2):
                a = random.randint(1,9)
                b = random.randint(1,9)
                c = random.randint(1,9)
                print(a,b,c)
                time.sleep(1)
            if w == 1:
                a = random.randint(1,9)
                b = random.randint(1,9)
                c = a
                print(a,b,c)
            if ft == 1:
                a = random.randint(1,9)
                b = random.randint(1,9)
                c = a
                print(a,b,c)
                ft = 0
            if a == b and b == c and a == c:
                wods.win()
                money.smw = 1
                money.money = money.money * a
                break
            if a == b or a == c or b == c:
                if a == b or a == c:
                    money.money = money.money + a
                    print("Money +",a)
                elif b == c:
                    money.money = money.money + b
                    print("Money +",b)
            d = a-b
            e = a-c
            f = b-a
            g = b-c
            h = c-a
            j = c-b
            check = 0
            if d > e and d > f and d > g and d > h and d >= j and check == 0:
                hairs = hairs - d
                print("Hairs -",d)
                check = 1
            if e > d and e > f and e >= g and e > h and e > j and check == 0:
                hairs = hairs - e
                print("Hairs -",e)
                check = 1
            if f > e and f > d and f > g and f >= h and f > j and check == 0:
                hairs = hairs - f
                print("Hairs -",f)
                check = 1
            if g >= e and g > f and g > d and g > h and g > j and check == 0:
                hairs = hairs - g
                print("Hairs -",g)
                check = 1
            if h > e and h >= f and h > g and h > d and h > j and check == 0:
                hairs = hairs - h
                print("Hairs -",h)
                check = 1
            if j > e and j > f and j > g and j > h and j >= d and check == 0:
                hairs = hairs - j
                print("Hairs -",j)
                check = 1
            if d >= e and d > f and d > g and d > h and d > j and check == 0:
                hairs = hairs - d
                print("Hairs -",d)
                check = 1
            if e >= d and e > f and e > g and e > h and e > j and check == 0:
                hairs = hairs - e
                print("Hairs -",e)
                check = 1
            if f > e and f > d and f >= g and f > h and f > j and check == 0:
                hairs = hairs - f
                print("Hairs -",f)
                check = 1
            if g > e and g >= f and g > d and g > h and g > j and check == 0:
                hairs = hairs - g
                print("Hairs -",g)
                check = 1
            if h > e and h > f and h > g and h > d and h >= j and check == 0:
                hairs = hairs - h
                print("Hairs -",h)
                check = 1
            if j > e and j > f and j > g and j >= h and j > d and check == 0:
                hairs = hairs - j
                print("Hairs -",j)
                check = 1