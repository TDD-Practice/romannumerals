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
    assert toroman(11) == 'XI'
    assert toroman(12) == 'XII'
    assert toroman(13) == 'XIII'
    assert toroman(14) == 'XIV'
    assert toroman(15) == 'XV'
    assert toroman(16) == 'XVI'
    assert toroman(17) == 'XVII'
    assert toroman(18) == 'XVIII'
    assert toroman(19) == 'XIX'
    assert toroman(20) == 'XX'


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
    assert fromroman('XI') == 11
    assert fromroman('XII') == 12
    assert fromroman('XIII') == 13
    assert fromroman('XIV') == 14
    assert fromroman('XV') == 15
    assert fromroman('XVI') == 16
    assert fromroman('XVII') == 17
    assert fromroman('XVIII') == 18
    assert fromroman('XIX') == 19
    assert fromroman('XX') == 20
