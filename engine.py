from character import Character
from item import Item


def main():
    fist = Item("fist", "punch", 0)

    sword = Item("sword", "slash", 10)
    print(sword)
    
    rope = Item("rope", "hang", -500)
    print(rope)

    bottle = Item("bottle", "throw at head", 1)
    print(bottle)

    charac = Character("test", 50, 15, 10, [fist])
    print(charac, charac.list_items(), sep="\n")
    
    charac2 = Character("test 2", 1000, 0, 0, [fist, sword, rope])
    print(charac2, charac2.list_items(), sep="\n")
    
    print(charac2.formatted_attack_result(2, charac))
    print(charac2)

    print(charac.formatted_attack_result(0, charac2))
    print(charac2)

if __name__ == "__main__":
    main()
