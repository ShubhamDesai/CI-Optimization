from geometry import area_of_circle,perimeter_of_rectangle,math

def test_area_of_circle():
    assert math.isclose(area_of_circle(1), math.pi)
    assert area_of_circle(0) == 0

def test_perimeter_of_rectangle():
    assert perimeter_of_rectangle(2, 3) == 10
    assert perimeter_of_rectangle(0, 0) == 0