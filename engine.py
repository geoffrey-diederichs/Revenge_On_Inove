from character import Character
from item import Item


def main():
    charac = Character.create_character("test")
    student1 = Character.create("student")

    print(student1.inflict_damages("coffee", charac), student1, charac, sep="\n")

    charac.add_item("rope")
    
    print(charac.inflict_damages("rope", student1), student1, charac, sep="\n")

    print(charac.inflict_damages("fist", student1), student1, charac, sep="\n")

if __name__ == "__main__":
    main()
