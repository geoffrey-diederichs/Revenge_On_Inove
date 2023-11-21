from __future__ import annotations


class Character:
    def __init__(self, name:str, max_health:int, attack:int, defense:int) -> None:
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
    
    def __str__(self) -> str:
        return f"{self._name}, {self._current_health}/{self._max_health}hp, {self._attack} attack, {self._defense} defense."

if __name__ == "__main__":
    pass
