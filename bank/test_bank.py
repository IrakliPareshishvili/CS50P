from bank import value

def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()

def test_return_zero():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_return_twenty():
    assert value("HI") == 20
    assert value("hola") == 20

def test_return_hundred():
    assert value("GOOD DAY") == 100
    assert value("good morning") == 100


if __name__ == "__main__":
    main()
