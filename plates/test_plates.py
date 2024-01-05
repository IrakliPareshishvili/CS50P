from plates import is_valid

def main():
    test_length()
    test_letters()
    test_number()
    test_zero()
    test_punctuation()

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

def test_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False



if __name__ == "__main__":
    main()
