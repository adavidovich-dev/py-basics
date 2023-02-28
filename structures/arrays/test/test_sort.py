"""
Sort test module
"""
from unittest import TestCase
from structures.arrays.simple import SimpleArray
from .data import sort_data


class BubbleSearchTestCase(TestCase):
    """
    Bubble sort test
    """

    def test_sort(self):
        """
        Sort test
        :return: nothing
        """
        for runner in sort_data:
            self._sort_scenario(runner['array'], runner['test'])

    def _sort_scenario(self, data, test_array):
        array = SimpleArray(len(data))
        for runner in data:
            array.add(runner)

        array.bubble_sort()
        for index in range(0, len(test_array)):
            assert array.value_at(index) == test_array[index]


class SelectSearchTestCase(TestCase):
    """
    Select sort test
    """

    def test_sort(self):
        """
        Sort test
        :return: nothing
        """
        for runner in sort_data:
            self._sort_scenario(runner['array'], runner['test'])

    def _sort_scenario(self, data, test_array):
        array = SimpleArray(len(data))
        for runner in data:
            array.add(runner)

        array.select_sort()
        for index in range(0, len(test_array)):
            assert array.value_at(index) == test_array[index]


class InsertSearchTestCase(TestCase):
    """
    Insert sort test
    """

    def test_sort(self):
        """
        Sort test
        :return: nothing
        """
        for runner in sort_data:
            self._sort_scenario(runner['array'], runner['test'])

    def _sort_scenario(self, data, test_array):
        array = SimpleArray(len(data))
        for runner in data:
            array.add(runner)

        array.insert_sort()
        for index in range(0, len(test_array)):
            assert array.value_at(index) == test_array[index]
