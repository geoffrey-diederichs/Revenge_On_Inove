from character import Character
from item import Item


def fight(charac:Character, enemy:Character) -> int:
    charac_items = charac.list_items_array()
    enemy_items = enemy.list_items_array()

    print(charac, "vs", enemy, " ", sep="\n")
    while (charac.is_alive() == 1) and (enemy.is_alive() == 1):
        print("You have :")
        for i in charac_items:
            print(" - ", i)
        """
        item = input("Choose an item to attack : ")
        while True:
            if item.isdigit == False:
                item = input("Please give a number : ")
            elif (int(item) < 1) or (int(item) > len(charac_items)):
                item = input("Please give a valid numer")
            else:
                break
        """

        charac.inflict_damages("fist", enemy)
        print(charac.get_name(), charac.health())
        print(enemy.get_name(), enemy.health(), "\n")

    if charac.is_alive() != 1:
        return 0
    return 1

def main():
    print("TEST ENGINE\n")

    print("Create your character")
    name = input("Name : ")
    attack = input("Attack : ")
    while attack.isdigit() == False:
        attack = input("Attack (a number please) : ")
    defense = input("Defense : ")
    while defense.isdigit() == False:
        defense = input("Defense (a number please) : ")
    attack = int(attack)
    defense = int(defense)
    
    charac = Character.create("character", name, attack, defense)
    student = Character.create("student")
    mentor = Character.create("mentor")
    teacher = Character.create("teacher")
    
    print("Round 1\n")
    if fight(charac, student) == 1:
        print("YOU WON !")
    else:
        print("You lost...")

if __name__ == "__main__":
    main()
