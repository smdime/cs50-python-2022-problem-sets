from seasons import calc_age, convert
from datetime import date

def test_calc_age():
    assert calc_age(date(2000, 1, 1)) == 12460320

def test_convert_age_to_mins_in_words():
    assert convert(calc_age(date(2000, 1, 1))) == "Twelve million, four hundred sixty thousand, three hundred twenty minutes"
