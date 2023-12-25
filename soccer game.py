import random
home_advantage = 85
away_disadvantage = 90

def goalPeriod(goalShot, h_goals, a_goals):
    if goalShot == 'y':
        shot_chance_home = random.randrange(1,100)
        shot_chance_away = random.randrange(1,100)
        if shot_chance_home > home_advantage: 
            h_goals += 1
        if shot_chance_away > away_disadvantage: 
            a_goals += 1
        print ("Home score: ", h_goals)
        print ("Away score: ", a_goals)
        print()
    return h_goals, a_goals

def main():
    home_goals = 0
    away_goals = 0

    for x in range (5, 91, 5):
        print(x,"th minute.")
        shot = input("Hit 'y' to take a shot on goal: ")
        goalPeriod(shot, home_goals, away_goals)

    # END OF REGULATION

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
