import random
home_advantage = 85
away_disadvantage = 90
home_goals = 0
away_goals = 0

def goalPeriod():
    shot_chance_home = random.randrange(1,100)
    shot_chance_away = random.randrange(1,100)
    if shot_chance_home > home_advantage: 
        home_goals += 1
    if shot_chance_away > away_disadvantage: 
        home_goals += 1
    print ("Home score: ", home_goals)
    print ("Away score: ", away_goals)
    print()

def main():
    shot = input("5th minute. Hit 'y' to take a shot on goal: ")
    goalPeriod()
    shot = input("10th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("15th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("20th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("25th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("30th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("35th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("40th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("45th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    if home_goals == away_goals:
        print("The score is tied at halftime.")
    elif home_goals > away_goals:
        print("You're winning at halftime!")
    elif home_goals < away_goals:
        print("You're losing at haltime. Time for some 2nd half adjustments.")

    print()

    shot = input("50th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("55th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("60th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("65th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("70th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("75th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("80th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("85th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    shot = input("90th minute. Hit 'y' to take a shot on goal: ")
    if shot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage:
            home_goals += 1
        if shot_chance_away > away_disadvantage:
            away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
    print()
    if home_goals == away_goals:
        overtime = print("The score is tied at end of regulation. Extra time will be played.")
        shot = input("95th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        print()
        shot = input("100th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        print()
        shot = input("105th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        print("That's the end of the 1st half of overtime. 2nd half to begin soon.")
        print()
        shot = input("110th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        print()
        shot = input("115th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        print()
        shot = input("120th minute. Hit 'y' to take a shot on goal: ")
        if shot == 'y':
            shot_chance_home = random.randrange(1,100)
            shot_chance_away = random.randrange(1,100)
            if shot_chance_home > home_advantage:
                home_goals += 1
            if shot_chance_away > away_disadvantage:
                away_goals += 1
        print("Home score: ",home_goals)
        print("Away score: ",away_goals)
        if home_goals == away_goals:
            overtime = print("The score is tied at end of overtime. We go to penalty shootout.")
        elif home_goals > away_goals:
            print("You won the game!")
        elif home_goals < away_goals:
            print("You lost the game. Perhaps it's time for a coaching change.") 

    elif home_goals > away_goals:
        print("You won the game!")
    elif home_goals < away_goals:
        print("You lost the game. Perhaps it's time for a coaching change.")
main()
