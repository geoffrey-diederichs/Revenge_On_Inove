from __future__ import annotations
from item import Item


class Character:
    def __init__(self, name:str, max_health:int, attack:int, defense:int, items:[Item]) -> None:
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
    def create(cls, name:str) -> Character:
        match name:
            case "student":
                return Character.create_student()
        return Character.create_student()

    @classmethod
    def create_character(cls, name:int) -> Character:
        new_charac = Character(name, 100, 20, 10, [])
        new_charac._items.append(Item.create("fist"))
        return new_charac

    @classmethod
    def create_student(cls) -> Character:
        new_student = Character("Student", 30, 10, 10, [])
        new_student._items.append(Item.create("fist"))
        new_student._items.append(Item.create("coffee"))
        return new_student

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
    
    def has_item(self, item:str) -> int:
        for i in self._items:
            if i._name == item:
                return 1 
        return 0

    def add_item(self, item:str) -> None:
        if self.has_item(item) == 0:
            self._items.append(Item.create(item))
    
    def remove_item(self, item:str) -> None:
        for i in self._items:
            if i._name == item:
                self._items.remove(i)

    def is_alive(self) -> int:
        if self._current_health > 0:
            return 1
        return 0

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
