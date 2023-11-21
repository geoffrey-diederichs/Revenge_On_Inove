from character import Character
from item import Item


def main():
    sword = Item("sword", "slash", "10")
    print(sword)
    
    rope = Item("rope", "hang himself", "-500")
    print(rope)

    bottle = Item("bottle", "throw at head", "1")
    print(bottle)

    charac = Character("test", 50, 15, 10, [])
    print(charac, charac.list_items(), sep="\n")
    
    charac2 = Character("test 2", 0, 0, 0, [sword, rope])
    print(charac2, charac2.list_items(), sep="\n")
    
    print(charac2.has_item(sword), charac2.has_item(bottle), charac.has_item(rope), sep="\n")

    charac.add_item(rope)
    print(charac.list_items(), charac.has_item(rope), sep="\n")
    charac.remove_item(rope)
    print(charac.has_item(rope), charac.list_items(), sep="\n")
    

if __name__ == "__main__":
    main()
