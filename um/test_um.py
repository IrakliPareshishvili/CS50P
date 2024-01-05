from um import count

def main():
    test_uplow()
    test_width()
    test_zero()

def test_uplow():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_width():
    assert count("yummi") == 0



def test_zero():
    assert count("hi um and") == 1
    assert count("um?") == 1


if __name__ == "__main__":
    main()
