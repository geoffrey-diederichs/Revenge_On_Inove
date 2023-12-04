from __future__ import annotations


class Item():
    def __init__(self, name:str, attack:int):
        self._name = name
        self._attack = attack

    def __str__(self) -> str:
        return f"{self._name}, {self._attack} attack."

    @classmethod
    def create(cls, key:str) -> Item:
        match key:
            case "fist":
                return Fist()
            case "coffee":
                return Coffee()
            case "rope":
                return Rope()
            case "trello":
                return Trello()
            case "wooclap":
                return Wooclap()
            case "survey_monkey":
                return Survey_monkey()
            case "mug_inove":
                return Mug_inove()
            case "shell":
                return Shell()
            case "inexistent":
                return Inexistent()
        return item.Fist()

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
        super().__init__("wooclap", 20)

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
        super().__init__("shell", 80)

class Arch(Item):
    def __init__(self) -> Item:
        super().__init__("arch", 50)

class Windaube(Item):
    def __init__(self) -> Item:
        super().__init__("windaube", 60)


if __name__ == "__main__":
    pass

