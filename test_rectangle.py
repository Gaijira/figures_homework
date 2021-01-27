import pytest
from figures import *


@pytest.mark.parametrize('rectangle_name,height,width', [('Rect1', 5, 6)])
def test_perimeter(rectangle_name, height, width):
    rectangle = Rectangle(rectangle_name, height, width)
    rectangle.count_perimeter()
    assert rectangle.perimeter == 22


@pytest.mark.parametrize('rectangle_name,height,width', [('Rect2', 7, 8)])
def test_area(rectangle_name, height, width):
    rectangle = Rectangle(rectangle_name, height, width)
    rectangle.count_area()
    assert rectangle.area == 56


@pytest.mark.parametrize('rectangle_name,height,width', [('Rect3', 10, 9)])
def test_name(rectangle_name, height, width):
    rectangle = Rectangle(rectangle_name, height, width)
    assert rectangle.name == rectangle_name


def test_angles():
    rectangle = Rectangle('Rect4', 10, 8)
    rectangle.count_angles()
    assert rectangle.angles == 4


@pytest.mark.parametrize('rectangle_name,height,width', [('Rect5', 10, 9)])
@pytest.mark.parametrize('rectangle2_name,height2,width2', [('Rect6', 11, 12)])
def test_add_area(rectangle_name, height, width, rectangle2_name, height2, width2):
    rectangle = Rectangle(rectangle_name, height, width)
    rectangle_2 = Rectangle(rectangle2_name, height2, width2)
    rectangle.count_area()
    rectangle_2.count_area()
    assert rectangle.add_area(rectangle_2) == 222
