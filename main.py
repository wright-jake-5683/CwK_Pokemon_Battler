import pokemon 
import moves
import helper_functions as hf

play = True
team = []

while (play == True):
    action, team = hf.mainLobby(team)

    match (action):
        case "Explore":
            while (action == "Explore"):
                if not team:
                    print("You have no pokemon left on your team, returning to Pokemon Center...")
                    action = ""
                else:
                    hf.startFight(team, True)
                    answer = input("Press 1 to keep exploring or press any other button to return to the Pokemon Center: \n")
                    try:
                        if (int(answer) != 1):
                            action = ""
                    except ValueError:
                            action = ""
            
