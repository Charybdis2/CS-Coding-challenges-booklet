def thief(p1, p2, p3, p4):
    pin = [p1, p2, p3, p4]
    for one in pin:
        for two in pin:
            if two == one:
                continue
            for three in pin:
                if three == one or three == two:
                    continue
                for four in pin:
                    if four == one or four == three or four == two:
                        continue
                    print(one+two+three+four)
        
    
p1, p2, p3, p4 = str(input("Please input the 4 digit pin: "))
thief(p1, p2, p3, p4)
