from __future__ import annotations


class Item():
    def __init__(self, name:str, attack_name:str, attack:int):
        if len(name) <= 0:
            name = "item"
        if len(attack_name) <= 0:
            attack_name = "item attack"
        self._name = name
        self._attack_name = attack_name
        self._attack = attack

    def __str__(self) -> str:
        return f"{self._name}, can {self._attack_name} with {self._attack} attack."