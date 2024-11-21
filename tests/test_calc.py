from ..calculate import calc
import pytest
def test_square_area_1():
    assert calc('square', 'area', [4]) == 16
def test_square_area_2():
    assert calc('square', 'area', [5]) == 25
def test_square_area_3():
    with pytest.raises(AssertionError):
        calc('square', 'area', [0])
def test_square_area_4():
    with pytest.raises(AssertionError):
        calc('square', 'area', [-1])
def test_square_perimeter_1():
    assert calc('square', 'perimeter', [3]) == 12
def test_square_perimeter_2():
    assert calc('square', 'perimeter', [6]) == 24
def test_square_perimeter_3():
    with pytest.raises(AssertionError):
        calc('square', 'perimeter', [0])
def test_square_perimeter_4():
    with pytest.raises(AssertionError):
        calc('square', 'perimeter', [-2])
def test_triangle_area_1():
    assert calc('triangle', 'area', [3, 4, 5]) == 6
def test_triangle_area_2():
    assert abs(calc('triangle', 'area', [8, 9, 12]) - 35.99913193397863) < 0.000000001
    #чтобы из-за погрешностей питона не возникло ошибок
def test_triangle_area_3():
    assert abs(calc('triangle', 'area', [7, 6, 10]) - 20.662465970933866) < 0.000000001
def test_triangle_area_4():
    with pytest.raises(AssertionError):
        calc('triangle', 'area', [3, 1, 10])
def test_triangle_area_5():
    with pytest.raises(AssertionError):
        calc('triangle', 'area', [-7, 0, 0])
def test_triangle_area_6():
    with pytest.raises(AssertionError):
        calc('triangle', 'area', [0, 0, 0])
def test_triangle_area_7():
    with pytest.raises(AssertionError):
        calc('triangle', 'area', [-7, -1, -1])
def test_triangle_perimeter_1():
    assert calc('triangle', 'perimeter', [3, 4, 5]) == 12
def test_triangle_perimeter_2():
    with pytest.raises(AssertionError):
        calc('triangle', 'perimeter', [1, 4, 1])
def test_triangle_perimeter_3():
    assert calc('triangle', 'perimeter', [4, 5, 8]) == 17
def test_triangle_perimeter_4():
    with pytest.raises(AssertionError):
        calc('triangle', 'perimeter', [0, 0, 0])
def test_triangle_perimeter_5():
    with pytest.raises(AssertionError):
        calc('triangle', 'perimeter', [-29, 100, 482])
def test_triangle_perimeter_6():
    with pytest.raises(AssertionError):
        calc('triangle', 'perimeter', [-9, -100, 0])
def test_triangle_perimeter_7():
    assert calc('triangle', 'perimeter', [12, 7, 6]) == 25
def test_circle_area_1():
    assert abs(calc('circle', 'area', [5]) - 78.53981633974483) < 0.000000001
def test_circle_area_2():
    assert abs(calc('circle', 'area', [18]) - 1017.8760197630929) < 0.000000001
def test_circle_area_3():
    with pytest.raises(AssertionError):
        calc('circle', 'area', [0])
def test_circle_area_4():
    with pytest.raises(AssertionError):
        calc('circle', 'area', [-10])
def test_circle_perimeter_1():
    assert abs(calc('circle', 'perimeter', [17]) - 106.81415022205297) < 0.000000001
def test_circle_perimeter_2():
    assert abs(calc('circle', 'perimeter', [108]) - 678.5840131753953) < 0.000000001
def test_circle_perimeter_3():
    with pytest.raises(AssertionError):
        calc('circle', 'perimeter', [0])
def test_circle_perimeter_4():
    with pytest.raises(AssertionError):
        calc('circle', 'perimeter', [-192383])