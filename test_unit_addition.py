import pytest
from addition import addition

def test_deux_positifs():
    assert addition(2,3) == 5

def test_negatif():
    assert addition(1, -1) == 0