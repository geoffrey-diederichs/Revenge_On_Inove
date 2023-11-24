from character import Character
from item import Item


def main():
    charac = Character.create("character", "test")
    student = Character.create("student")
    mentor = Character.create("mentor")
    teacher = Character.creat("teacher")

    print(mentor, mentor.list_items(), sep="\n")

if __name__ == "__main__":
    main()
