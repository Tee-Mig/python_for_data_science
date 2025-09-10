from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        family_name: str = "Baratheon",
        eye: str = "brown",
        hairs: str = "dark"
    ) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eye = eye
        self.hairs = hairs

    def die(self) -> None:
        self.is_alive = False

    def __str__(self) -> None:
        return f"Vector: ('Baratheon', '{self.eye}', '{self.hairs}')"

    def __repr__(self) -> None:
        return f"Vector: ('Baratheon', '{self.eye}', '{self.hairs}')"


class Lannister(Character):
    def __init__(
        self,
        first_name: str,
        is_alive: bool = True,
        family_name: str = "Lannister",
        eye: str = "blue",
        hairs: str = "light"
    ) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eye = eye
        self.hairs = hairs

    def die(self) -> None:
        self.is_alive = False

    def __repr__(self) -> None:
        return f"Vector: ('Lannister', '{self.eye}', '{self.hairs}')"

    def __str__(self) -> None:
        return f"Vector: ('Lannister', '{self.eye}', '{self.hairs}')"

    @classmethod
    def create_lannister(
        cls,
        first_name: str,
        is_alive: bool = True
    ) -> "Lannister":
        return cls(first_name)
