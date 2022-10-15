from um import count


def test_count_start():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_count_end():
    assert count("Um, thanks, um...") == 2
    assert count("um berlla um") == 2
    assert count("umberlla um") == 0


def test_count_middle():
    assert count("I have an umberlla") == 0


