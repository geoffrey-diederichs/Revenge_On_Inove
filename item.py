from __future__ import annotations


class Item():
    def __init__(self, name:str, attack_name:str, attack:int):
        self._name = name
        self._attack_name = attack_name
        self._attack = attack

    @classmethod
    def create(cls, key:str) -> Item:
        match key:
            case "fist":
                return Item.create_fist()
            case "coffee":
                return Item.create_coffee()
            case "sword":
                return Item.create_sword()
            case "rope":
                return Item.create_rope()
            case "wooclap":
                return Item.create_wooclap()
            case "shell":
                return Item.create_shell()
            case "inexistent":
                return Item.create_inexistent()
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
    
    @classmethod
    def create_wooclap(lcs) -> Item:
        return Item("wooclap", "make you answer a QCM", 10)

    @classmethod
    def create_shell(cls) -> Item:
        return Item("shell", "walk around with your shell open", 200)
    
    @classmethod
    def create_inexistent(cls) -> Item:
        return Item("inexistent", "not exist since there is no teachers at Inove", -1000)

    def __str__(self) -> str:
        return f"{self._name}, can {self._attack_name} with {self._attack} attack."

if __name__ == "__main__":
    pass
