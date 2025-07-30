# System Modules
import sys
import os
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


# Tests for area_of_circle
def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5

def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    radius = 0
    result = area_of_circle(radius)
    assert result == 0

def test_area_of_circle_negative_radius():
    """Test with a negative radius."""
    with pytest.raises(ValueError):
        area_of_circle(-5)

def test_area_of_circle_float_radius():
    """Test with a float radius."""
    radius = 2.5
    result = area_of_circle(radius)
    expected = 3.14159 * radius * radius
    assert abs(result - expected) < 1e-5


# Tests for get_nth_fibonacci
def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    result = get_nth_fibonacci(0)
    assert result == 0

def test_get_nth_fibonacci_one():
    """Test with n=1."""
    result = get_nth_fibonacci(1)
    assert result == 1

def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    result = get_nth_fibonacci(10)
    assert result == 55

def test_get_nth_fibonacci_negative():
    """Test with a negative input."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-1)

def test_get_nth_fibonacci_large():
    """Test with a large n."""
    result = get_nth_fibonacci(30)
    assert result == 832040

def test_get_nth_fibonacci_non_integer():
    """Test with a non-integer input."""
    with pytest.raises(TypeError):
        get_nth_fibonacci(5.5)
