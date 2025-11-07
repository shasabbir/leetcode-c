"""
Tests for Two Sum problem
"""

import pytest
from arrays.two_sum import two_sum


@pytest.mark.arrays
class TestTwoSum:
    def test_example_1(self):
        """Test with example case 1"""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        assert result == [0, 1]

    def test_example_2(self):
        """Test with example case 2"""
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        assert result == [1, 2]

    def test_example_3(self):
        """Test with example case 3"""
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        assert result == [0, 1]

    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = two_sum(nums, target)
        assert result == [2, 4]

    def test_zero_sum(self):
        """Test with zero target"""
        nums = [-1, 0, 1]
        target = 0
        result = two_sum(nums, target)
        assert result == [0, 2]
