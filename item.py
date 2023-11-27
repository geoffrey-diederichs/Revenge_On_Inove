from __future__ import annotations


class Item():
    def __init__(self, name:str, attack:int):
        self._name = name
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
        return Item("fist", 1)

    @classmethod
    def create_coffee(cls) -> Item:
        return Item("coffee", 3)

    @classmethod
    def create_sword(cls) -> Item:
        return Item("sword", 5)

    @classmethod
    def create_rope(cls) -> Item:
        return Item("rope", -500)
    
    @classmethod
    def create_wooclap(cls) -> Item:
        return Item("wooclap", 10)

    @classmethod
    def create_shell(cls) -> Item:
        return Item("shell", 200)
    
    @classmethod
    def create_inexistent(cls) -> Item:
        return Item("inexistent", -100000)

    def __str__(self) -> str:
        return f"{self._name}, {self._attack} attack."

class Fist(Item):
    def __init__(self) -> Item:
        super().__init__("fist", 1)

class Coffee(Item):
    def __init__(self) -> Item:
        super().__init__("coffee", 5)

class Rope(Item):
    def __init__(self) -> Item:
        super().__init__("rope", -1000)

class Trello(Item):
    def __init__(self) -> Item:
        super().__init__("trello", 10)

class Wooclap(Item):
    def __init__(self) -> Item:
        super().__init__("wooclap", 0)

class Inexistent(Item):
    def __init__(self) -> Item:
        super().__init__("inexistent", -1000000)

class Survey_monkey(Item):
    def __init__(self) -> Item:
        super().__init__("survey monkey", 20)

class Google(Item):
    def __init__(self) -> Item:
        super().__init__("google", 50)

class Mug_inove(Item):
    def __init__(self) -> Item:
        super().__init__("mug inove", -50)

class Shell(Item):
    def __init__(self) -> Item:
        super().__init__("shell", 50)

class Arch(Item):
    def __init__(self) -> Item:
        super().__init__("arch", 60)

class Windaube(Item):
    def __init__(self) -> Item:
        super().__init__("windaube", 70)

if __name__ == "__main__":
    pass
