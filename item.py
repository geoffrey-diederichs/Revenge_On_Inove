from __future__ import annotations


class Item():
    def __init__(self, name:str, attack_name:str, attack:int):
        self._name = name
        self._attack_name = attack_name
        self._attack = attack

    @classmethod
    def create_item(cls) -> Item:
        return Item("fist", "punch", 0)

    def __str__(self) -> str:
        return f"{self._name}, can {self._attack_name} with {self._attack} attack."
