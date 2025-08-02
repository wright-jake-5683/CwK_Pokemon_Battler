import random
import pokemon
import moves

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
                team.append(poke)
                count += 1
                print()
            case 2:
                name = input("Please give your new Charmander a name: \n")
                poke = pokemon.Charmander(name)
                team.append(poke)
                count += 1
                print()
            case 3:
                name = input("Please give your new Squirtle a name: \n")
                poke = pokemon.Squirtle(name)
                team.append(poke)
                count += 1
                print()
    return team

#---------------------------------------------------------------

def explorePrep(team):
        while (True):
            if len(team) < 3:
                print(f"It appears you only have {len(team)} pokemon on your team to go exploring with. Please select more Pokemon to start with \n")
                print("------------------------------")
                team = generateStartingPokemon(team)
                print("\nGreat, here is your team: \n ")
                for poke in team:
                    print(f"{poke.name} - Species: {poke.species}")
                    print("--------------------------------")

            ready = input("Are you ready to explore? (Y/N)\n")
            if (ready.upper().strip() == "Y"):
                action = "Explore"
                return action, team
            elif (ready.upper().strip() == "N"):
                action = ""
                return action, team
            else:
                print("Please enter 'Y' if you are ready to explore and 'N' if you would like to stay in the main lobby \n")

#---------------------------------------------------------------

def viewTeam(team):
    if not team:
        print("There are currently no pokemon on your team")
    else:
        for poke in team:
            print(f"{poke.name} - Species: {poke.species}")
            print("--------------------------------")
    action = ""
    return action, team

#---------------------------------------------------------------

def mainLobby(team):
    options = ["Explore", "View Team"]

    print("Welcome to the Pokemon center. Please select one of the following options by typing its corresponding number value: \n")
    for option in  options:
        print(f"{options.index(option) + 1}). {option}")
    print()
    try:
        optionSelected = int(input())
        if (optionSelected in range(len(options) + 1) and isinstance(optionSelected, int)):
            match (optionSelected):
                case 1: 
                    return explorePrep(team)
                case 2:
                    return viewTeam(team)
        else:
            return "", team
    except ValueError:
        print("Please enter in a valid integer corresponding to a valid option")
        return "", team

#---------------------------------------------------------------

def startFight(team, fight):
        enemy = generateWildPokemon()
        print(f"A Wild {enemy.species} has appeared...")
        print("------------------------------")
        print("Chose the pokemon you would like to fight with by typing their corresponding number")
        for character in team:
            print(f"{team.index(character) + 1}). {character.name}")
        selection = int(input())
        character = team[selection - 1]
        print(f"{character.name}'s health: {character.health}")
        print(f"Wild Pokemon's health: {enemy.health}")
        print("------------------------------")

        while(fight):
            print("Choose a move to attack by entering it's number...")
            move = playerMove(character)
            enemyMove = opponentMove(enemy)
            enemy.calculateDamage(move, character.attack, character.name)
            character.calculateDamage(enemyMove, enemy.attack, enemy.name)
            print(f"{character.name}'s health: {character.health}")
            print(f"Wild Pokemon's health: {enemy.health}")
            print("------------------------------")
            if (character.health == 0 and enemy.health == 0):
                print("Both parties have lost the fight...")
                team.remove(character)
                fight = False
                result = "lost"
            elif (enemy.health == 0):
                print("Enemy has been defeated...")
                print(f"You have acquired a new {enemy.species}. Please give your new pokemon a new:")
                name = input()
                poke = acquirePokemon(enemy, name)
                team.append(poke)
                fight = False
                result = "won"
            elif (character.health == 0):
                print("You have been defeated...")
                team.remove(character)
                fight = False
                result = "lost"
        return result

#---------------------------------------------------------------

def playerMove(character):
    for move in character.moveSet:
        print(f"{character.moveSet.index(move) + 1}). {move}")
    selection = int(input())
    if (selection in range(len(character.moveSet) + 1)):
        move = getattr(moves, character.moveSet[selection - 1])
    else:
        print(f"Value entered is out of range of available move options. Defaulting to basic move...")
        move = getattr(moves, character.moveSet[0])
    return move(character.element)
    

#---------------------------------------------------------------

def opponentMove(enemy):
    r = random.randint(0, len(enemy.moveSet) - 1)
    move = getattr(moves, enemy.moveSet[r])
    return move(enemy.element)

#---------------------------------------------------------------

def acquirePokemon(enemy, name):
    poke = getattr(pokemon, enemy.species)
    return poke(name)
