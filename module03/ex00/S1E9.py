from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class 1"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Your docstring for Constructor 1"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Your docstring for Method 1"""
        self.is_alive = False


class Stark(Character):
    """Your docstring for Class 2"""
    def die(self) -> None:
        """Your docstring for Method 2"""
        super().die()
