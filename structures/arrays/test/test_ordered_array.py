"""
Ordered arrays test module
"""
import time
from unittest import TestCase

import pytest

from structures.arrays.ordered import OrderedArray
from .data import search_sorted_data, add_sorted_data


class SearchTestCase(TestCase):
    """
    Search functionality tests
    """

    def test_search(self):
        """
        Binary search test
        :return:
        """
        for test_case in search_sorted_data:
            self._search_scenario(test_case)

    def _search_scenario(self, test_data,
                         is_measure=False):
        many_array = OrderedArray(len(test_data.list))
        for value in test_data.list:
            many_array.add(value)

        start_time = time.time()
        found_index = many_array.find(test_data.value)
        end_time = time.time()
        if is_measure:
            print(
                f"\n--- Element searching took {(end_time - start_time) * 1000} milliseconds "
                f"in {many_array.length}-length array---\n")
        assert found_index == test_data.index


class ArrayTestCase(TestCase):
    """
    Array actions tests
    """

    def test_creation(self):
        """
        Test array creation
        :return:
        """
        with pytest.raises(ValueError):
            OrderedArray(-1)

        zero_array = OrderedArray(0)
        assert zero_array.max_size == 0
        assert zero_array.length == 0
        assert zero_array.values() == ()

        single_array = OrderedArray(1)
        assert single_array.max_size == 1
        assert single_array.length == 0
        assert single_array.values() == ()

        an_array = OrderedArray(100)
        assert an_array.max_size == 100
        assert an_array.length == 0
        assert an_array.values() == ()

    def test_add(self):
        """
        Test array add element operation
        :return:
        """
        zero_array = OrderedArray(0)
        self.assertRaises(OverflowError, zero_array.add, 555)

        single_array = OrderedArray(1)
        single_array.add(1)
        assert single_array.max_size == 1
        assert single_array.length == 1
        assert single_array.values() == (1,)

        with pytest.raises(OverflowError):
            single_array.add(2)

        for test_case_data in add_sorted_data:
            self._add_scenario(test_case_data)

    def _add_scenario(self, test_case):
        many_array = OrderedArray(len(test_case.list) + 1)
        for value in test_case.list:
            many_array.add(value)
        assert many_array.max_size == len(test_case.list) + 1
        assert many_array.length == len(test_case.list)
        assert many_array.values() == test_case.list

        many_array.add(test_case.add_value)
        assert many_array.max_size == len(test_case.list) + 1
        assert many_array.length == len(test_case.list) + 1
        assert many_array.values() == test_case.check_list

    def test_delete(self):
        """
        Test array's delete operation
        :return:
        """
        zero_array = OrderedArray(0)
        zero_array.delete(-1)
        zero_array.delete(0)
        zero_array.delete(100)

        single_array = OrderedArray(1)
        single_array.delete(-1)
        single_array.delete(0)
        single_array.delete(1)
        single_array.delete(100)

        single_array.add(55)
        single_array.delete(55)
        assert single_array.max_size == 1
        assert single_array.length == 0
        assert single_array.values() == ()

        self._delete_scenario((1, 2, 3, 4, 5), 0, (1, 2, 3, 4, 5))
        self._delete_scenario((1, 2, 3, 4, 5), 1, (2, 3, 4, 5))
        self._delete_scenario((1, 2, 3, 4, 5), 2, (1, 3, 4, 5))
        self._delete_scenario((1, 2, 3, 4, 5), 5, (1, 2, 3, 4))
        self._delete_scenario(("a", "b", "c", "d", "e"), "c",
                              ("a", "b", "d", "e"))

    def _delete_scenario(self, values, index, test_values):
        many_array = OrderedArray(len(values))
        for value in values:
            many_array.add(value)
        many_array.delete(index)
        assert many_array.max_size == len(values)
        assert many_array.length == len(test_values)
        assert many_array.values() == test_values

    def test_value_at(self):
        """
        Test array's value at index operation
        :return:
        """
        zero_array = OrderedArray(0)
        self.assertRaises(IndexError, zero_array.value_at, -1)
        self.assertRaises(IndexError, zero_array.value_at, 0)
        self.assertRaises(IndexError, zero_array.value_at, 100)

        single_array = OrderedArray(1)
        self.assertRaises(IndexError, single_array.value_at, -1)
        self.assertRaises(IndexError, single_array.value_at, 0)
        self.assertRaises(IndexError, single_array.value_at, 1)
        self.assertRaises(IndexError, single_array.value_at, 100)

        a_value = "First"
        single_array.add(a_value)
        assert single_array.value_at(0) == a_value

        self._value_at_scenario([1, 2, 3, 4, 5], 0, 1)
        self._value_at_scenario([1, 2, 3, 4, 5], 2, 3)
        self._value_at_scenario([1, 2, 3, 4, 5], 4, 5)
        self._value_at_scenario(["a", "b", "c", "d", "e", "f"], 2,
                                "c")

    def _value_at_scenario(self, values, index, text_value):
        many_array = OrderedArray(len(values))
        for value in values:
            many_array.add(value)

        assert many_array.max_size == len(values)
        assert many_array.length == len(values)
        assert many_array.value_at(index) == text_value

    def test_index_of(self):
        """
        Test array's index of function
        :return:
        """
        zero_array = OrderedArray(0)
        assert zero_array.index_of(555) == -1

        single_array = OrderedArray(1)
        assert zero_array.index_of(555) == -1

        a_value = 1
        single_array.add(a_value)
        assert single_array.index_of(555) == -1
        assert single_array.index_of(a_value) == 0

        self._index_of_scenario((1, 2, 3, 4, 5), 1, 0)
        self._index_of_scenario((1, 2, 3, 4, 5), 3, 2)
        self._index_of_scenario((1, 2, 3, 4, 5), 5, 4)
        self._index_of_scenario(("a", "b", "c", "d", "e", "f"),
                                "b", 1)

    def _index_of_scenario(self, values, index_of_value, test_index_value):
        many_array = OrderedArray(len(values))
        for value in values:
            many_array.add(value)

        assert many_array.max_size == len(values)
        assert many_array.length == len(values)
        assert many_array.index_of(index_of_value) == test_index_value
