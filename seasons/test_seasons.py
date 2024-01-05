from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday("1991-04-21") == ("1991", "04", "21")
    assert check_birthday("1991-4-21") == None
    assert check_birthday("April 21, 1991") == None



if __name__ == "__main__":
    main()
