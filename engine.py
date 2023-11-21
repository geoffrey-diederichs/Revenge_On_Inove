from character import Character
from item import Item


def main():
    sword = Item("sword", "slash", "10")
    print(sword)
    
    rope = Item("rope", "hang himself", "-500")
    print(rope)

    charac = Character("test", 50, 15, 10, [])
    print(charac, charac.list_items(), sep="\n")
    
    charac2 = Character("test 2", 0, 0, 0, [sword, rope])
    print(charac2, charac2.list_items(), sep="\n")

if __name__ == "__main__":
    main()
