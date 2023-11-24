from __future__ import annotations


class Item():
    def __init__(self, name:str, attack_name:str, attack:int):
        self._name = name
        self._attack_name = attack_name
        self._attack = attack

    @classmethod
    def create(cls, item:str) -> Item:
        match item:
            case "fist":
                return Item.create_fist()
            case "coffee":
                return Item.create_coffee()
            case "sword":
                return Item.create_sword()
            case "rope":
                return Item.create_rope()
        return Item.create_fist()

    @classmethod
    def create_fist(cls) -> Item:
        return Item("fist", "punch", 1)

    @classmethod
    def create_coffee(cls) -> Item:
        return Item("coffee", "throw boiling coffee", 3)

    @classmethod
    def create_sword(cls) -> Item:
        return Item("sword", "slash", 5)

    @classmethod
    def create_rope(cls) -> Item:
        return Item("rope", "hang himself", -500)

    def __str__(self) -> str:
        return f"{self._name}, can {self._attack_name} with {self._attack} attack."

if __name__ == "__main__":
    pass
