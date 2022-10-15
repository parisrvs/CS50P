from numb3rs import validate

def test_validate_sp():
    assert validate('255.255.1.121') == True
    assert validate('192.168.1.0') == True
    assert validate('192.168.1.1') == True
    assert validate('192.168.123.1') == True


def test_validate():
    assert validate('672.7685.2132.6789') == False
    assert validate('256.256.256.256') == False
    assert validate('192.168.1.256') == False
    assert validate('255.255.255.255') == True


def test_validate_format():
    assert validate('10.0.0.0') == True
    assert validate('abcd.efgh.ijkl.mnop') == False
    assert validate('cat') == False
    assert validate('111') == False
    assert validate('255.255.255') == False


def test_validate_special():
    assert validate('0.0.0.0') == True