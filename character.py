from __future__ import annotations
from item import Item


class Character:
    def __init__(self, name:str, max_health:int, attack:int, defense:int, items:[Item]) -> None:
        if len(name) <= 0:
            name = "bot"
        if max_health <= 0:
            max_health = 100
        if attack < 0:
            attack = 10
        if defense < 0:
            defense = 10
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack = attack
        self._defense = defense
        self._items = items

    def __str__(self) -> str:
        return f"{self._name}, {self._current_health}/{self._max_health}hp, {self._attack} attack, {self._defense} defense, {len(self._items)} items."
    
    def list_items(self) -> str:
        nbr_items = len(self._items)
        if nbr_items == 0:
            return f"{self._name} has 0 items."
        result = f"{self._name} has {nbr_items} items :"
        for i in self._items:
            result += f"\n - {i}"
        return result

if __name__ == "__main__":
    pass
