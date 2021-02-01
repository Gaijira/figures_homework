import pytest
from figures import *


@pytest.mark.parametrize('triangle_name, triangle_side1, triangle_side2, triangle_side3', [('Triangle', 6, 5, 7)])
def test_perimeter(triangle_name, triangle_side1, triangle_side2, triangle_side3):
    triangle = Triangle(triangle_name, triangle_side1, triangle_side2, triangle_side3)
    triangle.count_perimeter()
    assert triangle.perimeter == 18


@pytest.mark.parametrize('triangle_name, triangle_side1, triangle_side2, triangle_side3 ', [('Triangle2', 7, 5, 6)])
def test_area(triangle_name, triangle_side1, triangle_side2, triangle_side3):
    triangle = Triangle(triangle_name, triangle_side1, triangle_side2, triangle_side3)
    triangle.count_perimeter()
    triangle.count_area()
    assert triangle.area == 14


@pytest.mark.parametrize('triangle_name, triangle_side1, triangle_side2, triangle_side3', [('Triangle3', 10, 11, 3)])
def test_name(triangle_name, triangle_side1, triangle_side2, triangle_side3):
    triangle = Triangle(triangle_name, triangle_side1, triangle_side2, triangle_side3)
    assert triangle_name == triangle.name


def test_angles():
    triangle = Triangle('Triangle4', 8, 9, 11)
    triangle.count_angles()
    assert triangle.angles == 3


@pytest.mark.parametrize('triangle_name, triangle_side1, triangle_side2, triangle_side3', [('Triangle11', 10, 15, 6)])
@pytest.mark.parametrize('triangle2_name, triangle2_side1, triangle2_side2, triangle2_side3',
                         [('Triangle2', 12, 10, 7)])
def test_add_area(triangle_name, triangle2_name, triangle_side1, triangle2_side1, triangle_side2, triangle2_side2,
                  triangle_side3, triangle2_side3):
    triangle = Triangle(triangle_name, triangle_side1, triangle_side2, triangle_side3)
    triangle_2 = Triangle(triangle2_name, triangle2_side1, triangle2_side2, triangle2_side3)
    triangle.count_perimeter()
    triangle_2.count_perimeter()
    triangle.count_area()
    triangle_2.count_area()
    assert triangle.add_area(triangle_2) == 54
