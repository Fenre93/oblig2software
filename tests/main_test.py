import pytest
from main import *

def test_division_allowed_by_four_and_not_hundred():
    assert is_year_leapyear(2000) == True
    assert is_year_leapyear(2004) == True
    assert is_year_leapyear(2024) == True

def test_division_allowed_by_four_hundred():
    assert is_year_leapyear(2000) == True
    assert is_year_leapyear(2004) == True
    assert is_year_leapyear(2024) == True

def test_division_not_allowed_by_four():
    assert is_year_leapyear(2001) == False
    assert is_year_leapyear(2007) == False
    assert is_year_leapyear(2009) == False

def test_division__allowed_by_hundred_and_not_four_hundred():
    assert is_year_leapyear(2002) == False
    assert is_year_leapyear(2005) == False
    assert is_year_leapyear(2009) == False
