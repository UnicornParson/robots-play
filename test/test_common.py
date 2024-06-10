import pytest
from ..common import *

def test_first_not_null():
	assert first_not_null([0,0,0,0,1,2,3]) == 1
	assert first_not_null([0,8,0,0,1,2,3]) == 8
	assert first_not_null([]) == None
	assert first_not_null(None) == None
	assert first_not_null([0]*100) == None

def test_not_null():
	assert not_null([0, 0, 0, 0, 1, 2, 3]) == [1, 2, 3]
	assert not_null([0, 8, 0, 0, 1, 2, 3]) == [8, 1, 2, 3]
	assert not_null([]) == []
	assert not_null([0] * 100) == []

def test_get_diff():
	assert get_diff([1,2,3], [1,4,5,6]) == [0,2,2]
	assert get_diff([1, 2, 3, 4], [1, 4, 5]) == [0, 2, 2]
	assert get_diff([], [1, 4, 5, 6]) == []
	assert get_diff([1, 2, 3], []) == []
	assert get_diff(None, None) == []

def test_nb_diff():
	assert nb_diff([1,2,3,4,5,6]) == [1]*5
	assert nb_diff([100]*10) == [0] * 9
	assert nb_diff([100]) == []
	assert nb_diff([]) == []
	assert nb_diff(None) == []

def test_normalize():
	assert normalize([0,1,2,3]) == [0,1,2,3]
	assert normalize([1, 2, 3]) == [0, 1, 2]
	assert normalize([2, 3, -1]) == [3, 4, 0]
