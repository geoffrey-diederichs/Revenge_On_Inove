from character import Character
from item import Item


def main():
    charac = Character.create_character("test")
    print(charac, charac.list_items(), sep="\n")
    
    student1 = Character.create("student")
    print(student1, student1.list_items(), sep="\n")
    
    student1.remove_item("coffee")
    print(student1.list_items())

if __name__ == "__main__":
    main()
