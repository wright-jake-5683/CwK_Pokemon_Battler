import random
import pokemon

def generateWildPokemon():
    r = random.randint(1,3)
    if (r == 1):
        wild = pokemon.Bulbasaur("Bulbasaur")
    elif (r == 2):
        wild = pokemon.Charmander("Charmander")
    elif (r == 3):
        wild = pokemon.Squirtle("Squirtle")
    return wild

#---------------------------------------------------------------

def generateStartingPokemon(team):
    count = 0
    limit = 3 - len(team)
    while (count < limit):
        species = int(input("Choose a species: \n" +
        "Press 1 for Bulbasaur \n" +
        "Press 2 for Charmander \n" +
        "Press 3 for Squirtle \n"))
        
        match (species):
            case 1:
                name = input("Please give your new Bulbasaur a name: \n")
                poke = pokemon.Bulbasaur(name)
                team[poke.name] = poke
                count += 1
                print()
            case 2:
                name = input("Please give your new Charmander a name: \n")
                poke = pokemon.Charmander(name)
                team[poke.name] = poke
                count += 1
                print()
            case 3:
                name = input("Please give your new Squirtle a name: \n")
                poke = pokemon.Squirtle(name)
                team[poke.name] = poke
                count += 1
                print()
    return team

#---------------------------------------------------------------

def explorePrep(team):
        if len(team) < 3:
            print(f"It appears you only have {len(team)} pokemon on your team to go exploring with. Please select more Pokemon to start with \n")
            print("------------------------------")
            team = generateStartingPokemon(team)
            print("\nGreat, here is your team: \n ")
            for poke in team.values():
                print(f"{poke.name} - House: {poke.house}")
                print("--------------------------------")

        ready = input("Are you ready to explore? (Y/N)\n")
        if (ready.upper().strip() == "Y"):
            explore = True
            return explore, team
        elif (ready.upper().strip() == "N"):
            explore = False
            return explore, team
        else:
            print("Please enter 'Y' if you are ready to explore and 'N' if you would like to stay in the main lobby \n")

#---------------------------------------------------------------

def viewTeam():
    pass

#---------------------------------------------------------------

def mainLobby(team):
    options = ["Explore", "View Team"]

    print("Welcome to the Pokemon center. Please select one of the following options by type its corresponding number value: \n")
    for option in  options:
        print(f"{options.index(option) + 1}). {option}")
    print()
    optionSelected = int(input())
    
    match (optionSelected):
        case 1: 
            action, team = explorePrep(team)
        case 2:
            viewTeam()