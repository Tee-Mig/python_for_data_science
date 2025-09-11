
from ft_calculator import Calculator


def subject_tests():
    a = [5, 10, 2]
    b = [2, 4, 3]
    Calculator.dotproduct(a, b)
    Calculator.add_vec(a, b)
    Calculator.sous_vec(a, b)


def main():
    subject_tests()
    return 0


if __name__ == "__main__":
    main()
