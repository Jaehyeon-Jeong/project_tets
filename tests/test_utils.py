# test_utils.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import is_shift_full

def test_shift_not_full():
    assert not is_shift_full(1)

def test_shift_full():
    assert is_shift_full(2)

def test_shift_over_capacity():
    assert is_shift_full(3)
