from S1E9 import Character, Stark


def subject_tests():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("hodor")
        print(hodor)
    except Exception as e:
        print(f"[Error]: {e}")


def main():
    subject_tests()
    return 0


if __name__ == "__main__":
    main()
