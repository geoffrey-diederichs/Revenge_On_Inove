import character
import random


def fight(charac:character.Main_charac, enemy:character) -> int :
    charac_items = charac.list_items_array()
    enemy_items = enemy.list_items_array()

    print(charac, "vs", enemy, " ", sep="\n")
    while (charac.is_alive() == 1) and (enemy.is_alive() == 1):
        print("You have :")
        for i in charac_items:
            print(" - ", i)
        
        item = input("Choose an item to attack : ")
        while True:
            if item.isdigit() == False:
                item = input("Please give a number : ")
            elif (int(item) < 1) or (int(item) > len(charac_items)):
                item = input("Please give a valid number : ")
            else:
                break
        damages = charac.inflict_damages(charac_items[int(item)-1], enemy)
        
        if damages > 1:
            print("You inflicted", damages, "damages")
        elif damages == 1:
            print("You inflicted 1 damage")
        elif damages == 0:
            print("Nothing happened")
        elif damages < 0:
            print("He countered and inflicted you", damages, "damages")
        
        randNbr = random.randint(0, len(enemy_items)-1)
        damages = enemy.inflict_damages(enemy_items[randNbr], charac)

        if damages > 1:
            print("He inflicted you", damages, "damages")
        elif damages == 1:
            print("He inflicted you 1 damage")
        elif damages == 0:
            print("Nothing happened")
        else:
            print("You countered him and inflicted", damages, "damages")
       
        print()
        print(charac.get_name(), " : ", charac.health())
        print(enemy.get_name(), " : ", enemy.health(), "\n")
    
    if charac.is_alive() == 1:
        return 0
    return 1

def floor0(charac:character.Main_charac) -> int:
    result = fight(charac, character.Student())
    if result == 1:
        return result
    charac.add_item("coffee")

    result = fight(charac, character.Depressed_student())
    if result == 1:
        return result
    charac.add_item("rope")

    result = fight(charac, character.School_referent())
    if result == 1:
        return result
    charac.add_item("trello")

    return 0

def main():
    print("TEST ENGINE\n")
    print("Create your character")
    name = input("Name : ")
    charac = character.Main_charac(name)
    
    result = 0
    while (result == 0):
        match (charac.get_level()):
            case 0:
                result = floor0(charac)
                charac.up_level()
            case 1:
                print("1")
            case 2:
                print("2")
            case 3:
                print("3")

    if result == 1:
        print("\nYOU LOST !!")
        exit()
    print("\nYOU WON !!")


if __name__ == "__main__":
    main()
