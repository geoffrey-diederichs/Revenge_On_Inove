from __future__ import annotations
import item


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
            result.append(i._name)
        return result
    
    def has_item(self, item:str) -> int:
        for i in self._items:
            if i._name == item:
                return 1 
        return 0

    def add_item(self, item_name:str) -> None:
        if self.has_item(item_name) == 0:
            self._items.append(item.Item.create(item_name))
    
    def remove_item(self, item:str) -> None:
        for i in self._items:
            if i._name == item:
                self._items.remove(i)

    def is_alive(self) -> int:
        if self._current_health > 0:
            return 1
        return 0

    def compute_damages(self, item:str, target:Character) -> int:
        for i in self._items:
            if i._name == item:
                return self._attack + i._attack - target._defense
        return self._attack - target._defense
    
    def take_damages(self, damages:int) -> None:
        self._current_health -= damages
        if self._current_health < 0:
            self._current_health = 0

    def inflict_damages(self, item:str, target:Character) -> int:
        if self.is_alive() == 0:
            return 0
        damages = self.compute_damages(item, target)
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

class Main_charac(Character):
    def __init__(self, name:str) -> Character:
        super().__init__(name, 100, 15, 15, [item.Fist()])
        self._level = 0
   
    def reset_health(self) -> None:
        self._current_health = self._max_health

    def get_level(self) -> int:
        return self._level

    def up_level(self) -> None:
        self.reset_health()
        self._level += 1
        self._attack += 10 
        self._defense += 10

class Student(Character):
    def __init__(self) -> Character:
        super().__init__("student", 50, 5, 10, [item.Fist()])

class Depressed_student(Character):
    def __init__(self) -> Character:
        super().__init__("depressed student", 50, 10, 10, [item.Coffee()])

class School_referent(Character):
    def __init__(self) -> Character:
        super().__init__("school referent", 100, 10, 10, [item.Trello(), item.Trello(), item.Wooclap()])

class Mentor(Character):
    def __init__(self) -> Character:
        super().__init__("mentor", 50, 25, 15, [item.Fist(), item.Wooclap()])

class Teacher(Character):
    def __init__(self) -> Character:
        super().__init__("teacher", 100, 1000, 15, [item.Inexistent()])

class Director(Character):
    def __init__(self) -> Character:
        super().__init__("director", 100, 25, 20, [item.Fist(), item.Fist(), item.Google()])

class Mentor2(Character):
    def __init__(self) -> Character:
        super().__init__("mentor 2", 100, 40, 20, [item.Wooclap(), item.Trello()])

class Mentor3(Character):
    def __init__(self) -> Character:
        super().__init__("mentor 3", 100, 0, 0, [item.Wooclap(), item.Trello(), item.Shell()])

class Network_teacher(Character):
    def __init__(self) -> Character:
        super().__init__("network teacher", 200, 40, 30, [item.Fist(), item.Arch(), item.Windaube()])


if __name__ == "__main__":
    pass
