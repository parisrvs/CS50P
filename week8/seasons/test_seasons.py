from seasons import is_valid, get_words, get_minutes



def test_is_valid():
    assert is_valid("2002-12-02") == True
    assert is_valid("200-12-02") == False
    assert is_valid("2002-2-02") == False
    assert is_valid("0002-12-02") == True
    assert is_valid("2002-12-1") == False
    assert is_valid("2222-13-02") == False
    assert is_valid("2222-11-42") == False


def test_get_words():
    assert get_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert get_words(1051200) == "One million, fifty-one thousand, two hundred"


def test_get_minutes():
    assert get_minutes("2021-08-05") == 525600
    assert get_minutes("2020-08-05") == 1051200
