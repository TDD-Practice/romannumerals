import pytest

from main import toroman, fromroman

toroman_table = [
    (1, 'I'),
    (2,'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (11, "XI"),
    (12, "XII"),
    (13, "XIII"),
    (14, "XIV"),
    (15, "XV"),
    (16, "XVI"),
    (17, "XVII"),
    (18, "XVIII"),
    (19, "XIX"),
    (20, 'XX')
]

fromroman_table = [
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('V', 5),
    ('VI', 6),
    ("VII", 7),
    ("VIII", 8),
    ("IX", 9),
    ("X", 10),
    ("XI", 11),
    ("XII", 12),
    ("XIII", 13),
    ("XIV", 14),
    ("XV", 15),
    ("XVI", 16),
    ("XVII", 17),
    ("XVIII", 18),
    ("XIX", 19),
    ('XX', 20)
]

@pytest.mark.parametrize('number, roman', toroman_table)
def test_toroman(number, roman):
    assert toroman(number) == roman

@pytest.mark.parametrize('roman, number', fromroman_table)
def test_fromroman(roman, number):
    assert fromroman(roman) == number