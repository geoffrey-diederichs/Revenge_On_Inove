from __future__ import annotations
from item import Item


class Character:
    def __init__(self, name:str="bot", max_health:int=0, attack:int=0, defense:int=0, items:[Item]=[]) -> None:
        if max_health <= 0:
            max_health = 100
        if attack < 0:
            attack = 0 
        if defense < 0:
            defense = 0
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack = attack
        self._defense = defense
        self._items = items
    
    @classmethod
    def create_character(cls) -> Character:
        new_charac = Character()
        new_charac._items.append(Item.create_item())
        return new_charac

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

    def add_item(self, item:Item) -> None:
        self._items.append(item)
    
    def has_item(self, item:Item) -> int:
        for i in self._items:
            if i == item:
                return 1
        return 0

    def remove_item(self, item:Item) -> None:
        if self.has_item(item) == 1:
            self._items.remove(item)
    
    def is_alive(self) -> None:
        pass

    def compute_damages(self, item:Item) -> int:
        return self._attack + item._attack
    
    def take_damages(self, damages:int) -> None:
        self._current_health -= damages
        if self._current_health < 0:
            self._current_health = 0

    def inflict_damages(self, item:int, target:Character) -> int:
        damages = self.compute_damages(self._items[item])
        if damages < 0:
            self.take_damages(-1*damages)
        elif damages > 0:
            target.take_damages(damages)
        return damages

    def formatted_attack_result(self, item:int, target:Character) -> str:
        result = self.inflict_damages(item, target)
        if result == 0:
            return "Nothing happened"
        if result > 0:
            return f"{self._name} has {self._items[item]._attack_name} {target._name} for {result} damages."
        if result < 0:
            return f"{self._name} has {self._items[item]._attack_name} himself for {result} damages."

if __name__ == "__main__":
    pass
