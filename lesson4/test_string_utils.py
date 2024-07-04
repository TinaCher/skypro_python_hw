import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("input_str, expected", [
    #POSITIVE
    ("skypro", "Skypro"),
    ("SkyPro", "Skypro"),
    ("", ""),
    ("hello world", "Hello world"),
    ("123abc", "123abc"),
    #NEGATIVE
    ("SKYPRO", "Skypro"),
    ("HeLLo", "Hello"),
    (" skypro", " skypro")
])
def test_capitilize(input_str, expected):
    utils = StringUtils()
    assert utils.capitilize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    #POSITIVE
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   ", ""),
    ("  hello world  ", "hello world  "),
    ("\t\tSkyPro", "\t\tSkyPro"),
    #NEGATIVE
    ("", ""),
    ("non-trimmed", "non-trimmed")
])
def test_trim(input_str, expected):
    utils = StringUtils()
    assert utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, delimiter, expected", [
    #POSITIVE
   ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("x;y;z", ";", ["x", "y", "z"]),
    ("apple|orange|banana", "|", ["apple", "orange", "banana"]),
    #NEGATIVE
    ("no delimiters", ",", ["no delimiters"]),
    ("one,two", " ", ["one,two"]),
    ("|edge|case|", "|", ["", "edge", "case", ""])
])
def test_to_list(input_str, delimiter, expected):
    utils = StringUtils()
    assert utils.to_list(input_str, delimiter) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    #POSITIVE
     ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    ("hello", "h", True),
    ("testing", "t", True),
    #NEGATIVE
    ("SkyPro", "k", False),
    ("Python", "z", False),
    (" ", " ", True)
])
def test_contains(input_str, symbol, expected):
    utils = StringUtils()
    assert utils.contains(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    #POSITIVE
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "X", "SkyPro"),
    ("hello", "l", "heo"),
    ("banana", "a", "bnn"),
    #NEGATIVE
    ("Python", "z", "Python"),
    ("test", "test", ""),
    ("", "k", "")
])
def test_delete_symbol(input_str, symbol, expected):
    utils = StringUtils()
    assert utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    #POSITIVE
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("hello", "h", True),
    ("goodbye", "g", True),
    #NEGATIVE
    (" ", " ", True),
    ("", "S", False)
])
def test_starts_with(input_str, symbol, expected):
    utils = StringUtils()
    assert utils.starts_with(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    #POSITIVE
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    #NEGATIVE
    ("", "o", False)
])
def test_end_with(input_str, symbol, expected):
    utils = StringUtils()
    assert utils.end_with(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, expected", [
    #POSITIVE
    ("", True),
    (" ", True),
    #NEGATIVE
    ("SkyPro", False),
    ("  content  ", False),
    ("\t", True),
])
def test_is_empty(input_str, expected):
    utils = StringUtils()
    assert utils.is_empty(input_str) == expected

@pytest.mark.parametrize("lst, joiner, expected", [
    #POSITIVE
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    #NEGATIVE
    ([], ", ", ""),
    ([1, 2, 3], None, "1, 2, 3"),
     (["a", "b"], "", "ab")
])
def test_list_to_string(lst, joiner, expected):
    utils = StringUtils()
    assert utils.list_to_string(lst, joiner) == expected
