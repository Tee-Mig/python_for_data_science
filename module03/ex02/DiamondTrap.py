from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str) -> None:
        super().__init__(first_name=first_name)

    def set_eyes(self, value: str) -> None:
        self.eye = value

    def get_eyes(self) -> str:
        return self.eye

    def set_hairs(self, value: str) -> None:
        self.hairs = value

    def get_hairs(self) -> str:
        return self.hairs
