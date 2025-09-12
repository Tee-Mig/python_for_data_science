class calculator:
    def __init__(self, values: list = None):
        if values is None:
            values = []
        self.result = values

    def __add__(self, object) -> None:
        self.result = [num + object for num in self.result]
        print(self.result)

    def __mul__(self, object) -> None:
        self.result = [num * object for num in self.result]
        print(self.result)

    def __sub__(self, object) -> None:
        self.result = [num - object for num in self.result]
        print(self.result)

    def __truediv__(self, object) -> None:
        if object != 0:
            self.result = [num / object for num in self.result]
            print(self.result)
        else:
            print("It's impossible to divide by 0")
