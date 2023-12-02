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

def floor(charac:character.Main_charac, data:[]) -> int:
    print(len(data)/2)
    for i in range(0, int(len(data)/2)-1):
        print(i*2, data[i*2], data[i*2+1])
        result = fight(charac, data[i*2])
        if result == 1:
            return result
        if data[(i*2)+1] != "":
            charac.add_item(data[(i*2)+1])
    
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
                data = [character.Student(), "coffee", character.Depressed_student(), "rope", character.School_referent(), "trello"]
                result = floor(charac, data)
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
