import os
from project import check_extensions, append_to_csv


def test_append_to_csv():
    title = "Test Video"
    views = 1000
    append_to_csv(title, views)
    assert os.path.exists("data.csv")
    with open("data.csv", "r") as file:
        lines = file.readlines()
        assert lines[0] == "Title,Views\n"
        assert lines[1] == f"{title},{views}\n"

def test_check_extensions_valid():
    assert check_extensions("https://www.youtube.com/watch?v=abcdefg")

def test_check_extensions_invalid():
    assert not check_extensions("https://www.invalid.com/invalid")


