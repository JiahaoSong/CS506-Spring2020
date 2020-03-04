import pytest
import random

from cs506 import determinant


def test_determinant():
    # sanity checks
    try:
        determinant.determinant([])
    except ValueError as e:
        assert str(e) == "The matrix should not be empty."
    try:
        determinant.determinant([[1,2], [1]])
    except ValueError as e:
        assert str(e) == "The matrix must be square."
    
    assert determinant.determinant([[1]]) == 1
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    assert determinant.determinant(matrix) == 0
