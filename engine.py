from character import Character
from item import Item

def main():
    charac = Character("test", 50, 15, 10)
    print(charac)

    sword = Item("sword", "slash", "10")
    print(sword)

if __name__ == "__main__":
    main()
