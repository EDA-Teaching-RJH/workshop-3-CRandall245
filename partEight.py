inventory = []

def dec1():
    choice = input("There is a dungeon entrance in front of you, do you enter? Y/N")
    if choice == "Y":
        dec2()
    elif choice == "N":
        print("You reject the call of adventure")
    else:
        print("error")

def dec2():
    choice = input("There is a split in the pathon the left and right. Where do you go? L/R")
    if choice == "L":
        dec3()
    elif choice == "R":
        print("you fall in a pitfall trap and die to punji sticks")
    else:
        print("error")

def dec3():
    choice = input("You find a spear lodged in a wall and a sword on the floor on the other side of a closed off room. Which do you grab? Sword/ Spear")
    if choice.lower().strip() == "spear":
        inventory.append("spear")
        dec4()
    elif choice.lower().strip() == "sword":
        inventory.append("sword") 
        dec4()
    else:
        print("error")

def dec4():
    choice = input("You hear growling and turn to see a dire wolf approaching you, do you attack or attempt to flee? A/F")
    if choice == "A" and "spear" in inventory:
        print("you manage to slay the direwolf with your weapons reach")
        dec5()
    elif choice == "A" and "sword" in inventory:
        print("you manage to slash the direwolf but it reaches you cuts your carotid in the process")
        print("you died")
    elif choice == "F":
        print("you search for an exit but the direwolf is guarding the only exit")
        dec4()
    else:
        print("error")

def dec5():
    choice = int(input("In slaying the dire wolf you see a passage you missed in the corridor that lead to a room with 3 chests which do you open? 1/2/3"))
    if choice == 1:
        print("you open the chest and find nothing, the dungeon begins to rumble and the ceiling begins to crumble and you flee with only your spear")
    elif choice == 2:
        print("you open the chest and are jumped upon by the chest as it turned out to be a mimic, killing you")
        print("you died")
    elif choice == 3:
        inventory.append("golden amulet")
        print("you open the chest and find a golden amulet, the dungeon begins to rumble and the ceiling begins to crumble and you flee with only your spear and amulet")
    else:
        print("error")



dec1()