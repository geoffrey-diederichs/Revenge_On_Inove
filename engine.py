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
    
    charac = Character.create_character("test")
    print(charac, charac.list_items(), sep="\n")

if __name__ == "__main__":
    main()
