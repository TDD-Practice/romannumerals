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
    (20, 'XX'),
    (21, 'XXI'),
    (22, 'XXII'),
    (23, 'XXIII'),
    (24, 'XXIV'),
    (25, 'XXV'),
    (51, 'LI'),
    (55, 'LV'),
    (56, 'LVI'),
    (59, 'LIX'),
    (91, 'XCI'),
    (95, 'XCV'),
    (96, 'XCVI'),
    (99, 'XCIX')
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
    ('XX', 20),
    ('XXI', 21),
    ('XXII', 22),
    ('XXIII', 23),
    ('XXIV', 24),
    ('XXV', 25),
    ('LI', 51),
    ('LV', 55),
    ('LVI', 56),
    ('LIX', 59),
    ('XCI', 91),
    ('XCV', 95),
    ('XCVI', 96),
    ('XCIX', 99)
]

@pytest.mark.parametrize('roman, number', fromroman_table)
def test_fromroman(roman, number):
    assert fromroman(roman) == number

@pytest.mark.parametrize('number, roman', toroman_table)
def test_toroman(number, roman):
    assert toroman(number) == roman