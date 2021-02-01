from figures import *
import pytest


@pytest.mark.parametrize('circle_name, radius', [('Circle', 7)])
def test_name(circle_name, radius):
    circle = Circle(circle_name, radius)
    assert circle.name == circle_name


@pytest.mark.parametrize('circle_name, radius', [('Circle1', 5)])
def test_perimeter(circle_name, radius):
    circle = Circle(circle_name, radius)
    circle.count_perimeter()
    assert circle.perimeter == 31


@pytest.mark.parametrize('circle_name, radius', [('Circle2', 7)])
def test_area(circle_name, radius):
    circle = Circle(circle_name, radius)
    circle.count_area()
    assert circle.area == 153


def test_angles():
    circle = Circle('Circle', 6)
    circle.count_angles()
    assert circle.angles == 0


@pytest.mark.parametrize('circle1_name, radius_1', [('Circle1', 7)])
@pytest.mark.parametrize('circle2_name, radius_2', [('Circle2', 4)])
def test_add_area(circle1_name, radius_1, circle2_name, radius_2):
    circle_1 = Circle(circle1_name, radius_1)
    circle_2 = Circle(circle2_name, radius_2)
    circle_1.count_area()
    circle_2.count_area()
    assert circle_1.add_area(circle_2) == 203
