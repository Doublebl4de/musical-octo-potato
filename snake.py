import random as r
import time as t
die = 0
w = 0
a = 0
s = 0
d = 0
score = 0
f = r.randint(1,81)
sn = 1
snl = [-100, 41]
alive = 1
die = 0
hdir = 1
phdir = 0
list1 = [9,18,27,36,45,54,63,72]
list2 = [1,10,19,28,37,46,55,64,73]

while True:
            if f in snl:
                f = r.randint(1,81)
            else:
                break
pos = [0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0]
pos[f] = -1
pos[snl[1]] = hdir
print("###########")
for i in range(1,82):
            
            if pos[i] == 0:
                
                if i in list1:
                    print(" #",end ="\n")
                elif i in list2:
                    print("# ",end ="")
                elif i == 81:
                    print(" #\n###########",end ="\n\n\n")
                else:
                    print(" ",end ="")
            
            if pos[i] == 1:
                if i in list1:
                    print("˄#",end ="\n")
                elif i in list2:
                    print("#˄",end ="")
                elif i == 81:
                    print("˄#\n###########",end ="\n\n\n")
                else:
                    print("˄",end ="")
            if pos[i] == 2:
                if i in list1:
                    print("˂#",end ="\n")
                elif i in list2:
                    print("#˂",end ="")
                elif i == 81:
                    print("˂#\n###########",end ="\n\n\n")
                else:
                    print("˂",end ="")
            if pos[i] == 3:
                if i in list1:
                    print("˅#",end ="\n")
                elif i in list2:
                    print("#˅",end ="")
                elif i == 81:
                    print("˅#\n###########",end ="\n\n\n")
                else:
                    print("˅",end ="")
            if pos[i] == 4:
                if i in list1:
                    print("˃#",end ="\n")
                elif i in list2:
                    print("#˃",end ="")
                elif i == 81:
                    print("˃#\n###########",end ="\n\n\n")
                else:
                    print("˃",end ="")
            
            if pos[i] == -1:
                if i in list1:
                    print("o#",end ="\n")
                elif i in list2:
                    print("#o",end ="")
                elif i == 81:
                    print("o#\n###########",end ="\n\n\n")
                else:
                    print("o",end ="")
while True:
    if alive == 1:
        alive = 0
        while True:
            
            w = 0
            a = 0
            s = 0
            d = 0
            dlen = 0
            while True:
                dire = input()
                dire.lower
                dlen = len(dire)
                if dlen == 1:
                    break
            w = dire.count("w")
            a = dire.count("a")
            s = dire.count("s")
            d = dire.count("d")



            
                
            lsnl = len(snl) - 1
            if w == 1:
                phdir = hdir
                hdir = 1
                for i in range(1, lsnl + 1):
                    if lsnl - i == 0:
                        
                        if snl[lsnl - (i-1)] <= 9:
                            die = 1
                        else:
                            snl[lsnl - (i-1)] = snl[lsnl - (i-1)] - 9
                        
                    else:
                        snl[lsnl - (i-1)] = snl[lsnl  - (i-1) - 1]
            if a == 1:
                phdir = hdir
                hdir = 2
                for i in range(1, lsnl + 1):
                    if lsnl - i == 0:
                        
                        if snl[lsnl - (i-1)] == 1 or snl[lsnl - (i-1)] == 10 or snl[lsnl - (i-1)] == 19 or snl[lsnl - (i-1)] == 28 or snl[lsnl - (i-1)] == 37 or snl[lsnl - (i-1)] == 46 or snl[lsnl - (i-1)] == 55 or snl[lsnl - (i-1)] == 64 or snl[lsnl - (i-1)] == 73:
                            die = 1
                        else:
                            snl[lsnl - (i-1)] = snl[lsnl - (i-1)] - 1
                        
                    else:
                        snl[lsnl - (i-1)] = snl[lsnl  - (i-1) - 1]

            if s == 1:
                phdir = hdir
                hdir = 3
                for i in range(1, lsnl + 1):
                    if lsnl - i == 0:
                        
                        if snl[lsnl - (i-1)] >= 73:
                            die = 1
                        else:
                            snl[lsnl - (i-1)] = snl[lsnl - (i-1)] + 9
                        
                    else:
                        snl[lsnl - (i-1)] = snl[lsnl  - (i-1) - 1]
            if d == 1:
                phdir = hdir
                hdir = 4
                for i in range(1, lsnl + 1):
                    if lsnl - i == 0:
                        if snl[lsnl - (i-1)] == 9 or snl[lsnl - (i-1)] == 18 or snl[lsnl - (i-1)] == 27 or snl[lsnl - (i-1)] == 36 or snl[lsnl - (i-1)] == 45 or snl[lsnl - (i-1)] == 54 or snl[lsnl - (i-1)] == 63 or snl[lsnl - (i-1)] == 72 or snl[lsnl - (i-1)] == 81:
                            die = 1
                            print(die)
                        else:
                            snl[lsnl - (i-1)] = snl[lsnl - (i-1)] + 1
                        
                    else:
                        snl[lsnl - (i-1)] = snl[lsnl  - (i-1) - 1]
            
            head = snl[1]
            if snl.count(head) == 2:
                if lsnl != 2:
                    
                    die = 1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if snl[1] == f:
                snl.append(snl[lsnl])
                score = score + 1
                f = r.randint(1,81)
                
                while True:
                    if f in snl:
                        f = r.randint(1,81)
                    else:
                        break
            #print(snl)
            pos = [0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0]
            for i in range(0,lsnl):
                
                pos[f] = -1
                pos[snl[1]] = hdir
                print("###########")
                if lsnl >= 2:
                    if pos[snl[lsnl-i]] == pos[snl[lsnl]]:
                        if snl[lsnl - 1] == snl[lsnl] - 9 or snl[lsnl - 1] == snl[lsnl] + 9:
                            pos[snl[lsnl]] = 5
                        if snl[lsnl - 1] == snl[lsnl] - 1 or snl[lsnl - 1] == snl[lsnl] + 1:
                             pos[snl[lsnl]] = 6
                    else:
                        if snl[lsnl - i - 1] == snl[lsnl - i] - 9:
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 9:
                                pos[snl[lsnl - i]] = 5
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 1:
                                pos[snl[lsnl - i]] = 7
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 1:
                                pos[snl[lsnl - i]] = 8
                        if snl[lsnl - i - 1] == snl[lsnl - i] + 9:
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 9:
                                pos[snl[lsnl - i]] = 5
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 1:
                                pos[snl[lsnl - i]] = 9
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 1:
                                pos[snl[lsnl - i]] = 10
                        if snl[lsnl - i - 1] == snl[lsnl - i] - 1:
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 1:
                                pos[snl[lsnl - i]] = 6
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 9:
                                pos[snl[lsnl - i]] = 7
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 9:
                                pos[snl[lsnl - i]] = 9
                        if snl[lsnl - i - 1] == snl[lsnl - i] + 1:
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 1:
                                pos[snl[lsnl - i]] = 6
                            if snl[lsnl - i + 1] == snl[lsnl - i] - 9:
                                pos[snl[lsnl - i]] = 8
                            if snl[lsnl - i + 1] == snl[lsnl - i] + 9:
                                pos[snl[lsnl - i]] = 10
            for i in range(1,82):
                
                if pos[i] == 0:
                
                    if i in list1:
                        print(" #",end ="\n")
                    elif i in list2:
                        print("# ",end ="")
                    elif i == 81:
                        print(" #\n###########",end ="\n\n\n")
                    else:
                        print(" ",end ="")
            
                if pos[i] == 1:
                    if i in list1:
                        print("˄#",end ="\n")
                    elif i in list2:
                        print("#˄",end ="")
                    elif i == 81:
                        print("˄#\n###########",end ="\n\n\n")
                    else:
                        print("˄",end ="")
                if pos[i] == 2:
                    if i in list1:
                        print("˂#",end ="\n")
                    elif i in list2:
                        print("#˂",end ="")
                    elif i == 81:
                        print("˂#\n###########",end ="\n\n\n")
                    else:
                        print("˂",end ="")
                if pos[i] == 3:
                    if i in list1:
                        print("˅#",end ="\n")
                    elif i in list2:
                        print("#˅",end ="")
                    elif i == 81:
                        print("˅#\n###########",end ="\n\n\n")
                    else:
                        print("˅",end ="")
                if pos[i] == 4:
                    if i in list1:
                        print("˃#",end ="\n")
                    elif i in list2:
                        print("#˃",end ="")
                    elif i == 81:
                        print("˃#\n###########",end ="\n\n\n")
                    else:
                        print("˃",end ="")
                if pos[i] == 5:
                    if i in list1:
                        print("|#",end ="\n")
                    elif i in list2:
                        print("#|",end ="")
                    elif i == 81:
                        print("|#\n###########",end ="\n\n\n")
                    else:
                        print("|",end ="")
                if pos[i] == 6:
                    if i in list1:
                        print("–#",end ="\n")
                    elif i in list2:
                        print("#–",end ="")
                    elif i == 81:
                        print("–#\n###########",end ="\n\n\n")
                    else:
                        print("–",end ="")
                if pos[i] == 7:
                    if i in list1:
                        print("˼#",end ="\n")
                    elif i in list2:
                        print("#˼",end ="")
                    elif i == 81:
                        print("˼#\n###########",end ="\n\n\n")
                    else:
                        print("˼",end ="")
                if pos[i] == 8:
                    if i in list1:
                        print("˻#",end ="\n")
                    elif i in list2:
                        print("#˻",end ="")
                    elif i == 81:
                        print("˻#\n###########",end ="\n\n\n")
                    else:
                        print("˻",end ="")

                if pos[i] == 9:
                    if i in list1:
                        print("˺#",end ="\n")
                    elif i in list2:
                        print("#˺",end ="")
                    elif i == 81:
                        print("˺#\n###########",end ="\n\n\n")
                    else:
                        print("˺",end ="")

                if pos[i] == 10:
                    if i in list1:
                        print("˹#",end ="\n")
                    elif i in list2:
                        print("#˹",end ="")
                    elif i == 81:
                        print("˹#\n###########",end ="\n\n\n")
                    else:
                        print("˹",end ="")
                
                if pos[i] == -1:
                    if i in list1:
                        print("o#",end ="\n")
                    elif i in list2:
                        print("#o",end ="")
                    elif i == 81:
                        print("o#\n###########",end ="\n\n\n")
                    else:
                        print("o",end ="")
            print("Score:",score)
            if score == 80:
                print("You win!")
                die = 1
            if die == 1:
                score = 0
                f = r.randint(1,81)
                sn = 1
                snl = [0, 41]
                alive = 1
                print("You died")
                die = 0
                break
