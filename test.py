import random
playerHP = 0
enemyHP = 0
def attack(player, playerMoves, enemy, enemyMoves):
    '''Handles the characters fighting. Returns false when one of the characters has been defeated'''
    global playerHP, enemyHP
    # get move from player.
    defense = ["shield", "dodge"]
    playerMove = ""
    playerDefense = ""
    while playerMove not in playerMoves:
        print("Possible moves:", sorted(playerMoves.keys()))
        playerMove = input("Enter a move: ")
        if playerMove not in playerMoves:
            print("Invalid input.", sorted(playerMoves.keys()))
    playerDamage = random.randint(playerMoves[playerMove][0], playerMoves[playerMove][1])
    while playerDefense not in defense:
        print("Possible defense:", defense)
        playerDefense = input("Enter a defense: ")
        if playerDefense not in defense:
            print("Invalid input.", defense)
