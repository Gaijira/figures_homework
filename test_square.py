import pytest
from figures import *


@pytest.mark.parametrize('square_name,square_side', [('Square1', 6)])
def test_perimeter(square_name, square_side):
    square = Square(square_name, square_side)
    square.count_perimeter()
    assert square.perimeter == 24


@pytest.mark.parametrize('square_name, square_side', [('Square2', 8)])
def test_area(square_name, square_side):
    square = Square(square_name, square_side)
    square.count_area()
    assert square.area == 64


@pytest.mark.parametrize('square_name, square_side', [('Square3', 10)])
def test_name(square_name, square_side):
    square = Square(square_name, square_side)
    assert square.name == square_name


def test_angles():
    square = Square('Square4', 8)
    square.count_angles()
    assert square.angles == 4


@pytest.mark.parametrize('square_name,square_side', [('Square', 10)])
@pytest.mark.parametrize('square2_name,square2_side', [('Square2', 12)])
def test_add_area(square_name, square_side, square2_name, square2_side):
    square = Square(square_name, square_side)
    square_2 = Square(square2_name, square2_side)
    square.count_area()
    square_2.count_area()
    assert square.add_area(square_2) == 244
