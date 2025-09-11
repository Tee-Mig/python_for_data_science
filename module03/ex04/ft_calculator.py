class Calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(sum([a * b for a, b in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print([float(a + b) for a, b in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print([float(a - b) for a, b in zip(V1, V2)])
