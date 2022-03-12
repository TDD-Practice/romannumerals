import pytest

from main import toroman, fromroman

def test_toroman():
    assert toroman(1) == 'I'
    assert toroman(2) == 'II'
    assert toroman(3) == 'III'
    assert toroman(4) == 'IV'
    assert toroman(5) == 'V'
    assert toroman(6) == 'VI'
    assert toroman(7) == 'VII'
    assert toroman(8) == 'VIII'
    assert toroman(9) == 'IX'
    assert toroman(10) == 'X'


def test_fromroman():
    assert fromroman('I') == 1
    assert fromroman('II') == 2
    assert fromroman('III') == 3
    assert fromroman('IV') == 4
    assert fromroman('V') == 5
    assert fromroman('VI') == 6
    assert fromroman('VII') == 7
    assert fromroman('VIII') == 8
    assert fromroman('IX') == 9
    assert fromroman('X') == 10