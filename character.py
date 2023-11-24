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
    def create(cls, key:str, name:str="", attack:int=0, defense:int=0) -> Character:
        match key:
            case "character":
                return Character.create_character(name, attack, defense)
            case "student":
                return Character.create_student()
            case "mentor":
                return Character.create_mentor()
            case "teacher":
                return Character.create_teacher()
        return Character.create_student()

    @classmethod
    def create_character(cls, name:int, attack:int, defense:int) -> Character:
        return Character(name, 100, attack, defense, [Item.create("fist")])

    @classmethod
    def create_student(cls) -> Character:
        return Character("Student", 30, 10, 10, [Item.create("fist"), Item.create("coffee")])

    @classmethod
    def create_mentor(cls) -> Character:
        return Character("Mentor", 50, 20, 10, [Item.create("fist"), Item.create("wooclap")])

    @classmethod
    def create_teacher(cls) -> Character:
        return Character("Teacher", 1000, 50, 20, [Item.create("inexistent")])

    def __str__(self) -> str:
        return f"{self._name}, {self._current_health}/{self._max_health}hp, {self._attack} attack, {self._defense} defense, {len(self._items)} items."
   
    def get_name(self) -> str:
        return self._name

    def health(self) -> str:
        return f"{self._current_health}/{self._max_health}hp"

    def list_items(self) -> str:
        nbr_items = len(self._items)
        if nbr_items == 0:
            return f"{self._name} has 0 items."
        result = f"{self._name} has {nbr_items} items :"
        for i in self._items:
            result += f"\n - {i}"
        return result
    
    def list_items_array(self) -> [str]:
        result = []
        for i in self._items:
            print(i)
            result.append(i._name)
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

    def compute_damages(self, item:str) -> int:
        for i in self._items:
            if i._name == item:
                return self._attack + i._attack
        return self._attack
    
    def take_damages(self, damages:int) -> None:
        self._current_health -= damages
        if self._current_health < 0:
            self._current_health = 0

    def inflict_damages(self, item:str, target:Character) -> int:
        if self.is_alive() == 0:
            return 0
        damages = self.compute_damages(item)
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
