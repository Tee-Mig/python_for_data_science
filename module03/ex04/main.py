
from ft_calculator import calculator


def subject_tests():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


def main():
    subject_tests()
    return 0


if __name__ == "__main__":
    main()
