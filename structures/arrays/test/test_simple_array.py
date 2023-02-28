"""
Simple array test module
"""
import time
from unittest import TestCase

import pytest

from structures.arrays.simple import SimpleArray
from .data import search_sorted_data, search_unsorted_data, SearchUnitData


class SearchTestCase(TestCase):
    """
    Search functionality tests
    """

    def test_binary_search(self):
        """
        Binary search test
        :return:
        """
        values = (5, 4, 3, 2, 1)
        an_array = SimpleArray(len(values))
        for value in values:
            an_array.add(value)
        with pytest.raises(RuntimeError):
            an_array.binary_search(4)

        search_method_name = "binary_search"
        for test_case in search_sorted_data:
            self._search_scenario(test_case, search_func_name=search_method_name)

    def test_linear_search(self):
        """
        Linear search test
        :return:
        """
        search_method_name = "linear_search"
        self._search_scenario(SearchUnitData([], 0, -1),
                              search_func_name=search_method_name)

        for test_case in search_sorted_data:
            self._search_scenario(test_case, search_func_name=search_method_name)
        for test_case in search_unsorted_data:
            self._search_scenario(test_case, search_func_name=search_method_name)

    def _search_scenario(self, test_data, search_func_name,
                         is_measure=False):
        many_array = SimpleArray(len(test_data.list))
        for value in test_data.list:
            many_array.add(value)
        search_function = many_array.__getattribute__(search_func_name)

        start_time = time.time()
        found_index = search_function(test_data.value)
        end_time = time.time()
        if is_measure:
            print(
                f"\n---{search_func_name} took {(end_time - start_time) * 1000} milliseconds "
                f"to find in {many_array.length}-length array---\n")
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
            SimpleArray(-1)

        zero_array = SimpleArray(0)
        assert zero_array.max_size == 0
        assert zero_array.length == 0
        assert zero_array.values() == ()

        single_array = SimpleArray(1)
        assert single_array.max_size == 1
        assert single_array.length == 0
        assert single_array.values() == ()

        an_array = SimpleArray(100)
        assert an_array.max_size == 100
        assert an_array.length == 0
        assert an_array.values() == ()

    def test_add(self):
        """
        Test array add element operation
        :return:
        """
        zero_array = SimpleArray(0)
        self.assertRaises(OverflowError, zero_array.add, 555)

        self._add_scenario(555, (1, 2, 3, 4, 5, 6, 7, 8, 9))
        self._add_scenario("One value", ("First", "Second", "Third", "Forth", "Fifth"))

    def _add_scenario(self, one_value, many_values):
        single_array = SimpleArray(1)
        single_array.add(one_value)
        assert single_array.max_size == 1
        assert single_array.length == 1
        assert single_array.values() == (one_value,)

        self.assertRaises(OverflowError, single_array.add, one_value)

        many_array = SimpleArray(len(many_values))
        for value in many_values:
            many_array.add(value)
        assert many_array.max_size == len(many_values)
        assert many_array.length == len(many_values)
        assert many_array.values() == many_values

        many_extra_array = SimpleArray(len(many_values) + 16)
        for value in many_values:
            many_extra_array.add(value)
        assert many_extra_array.max_size == len(many_values) + 16
        assert many_extra_array.length == len(many_values)
        assert many_extra_array.values() == many_values

    def test_set(self):
        """
        Test array's set element operation
        :return:
        """
        set_value = "A value"
        zero_array = SimpleArray(0)
        self.assertRaises(IndexError, zero_array.set, -1, set_value)
        self.assertRaises(IndexError, zero_array.set, 0, set_value)
        self.assertRaises(IndexError, zero_array.set, 100, set_value)

        single_array = SimpleArray(1)
        self.assertRaises(IndexError, single_array.set, -1, set_value)
        self.assertRaises(IndexError, single_array.set, 0, set_value)
        self.assertRaises(IndexError, single_array.set, 1, set_value)
        self.assertRaises(IndexError, single_array.set, 100, set_value)

        single_array.add(555)
        assert single_array.max_size == 1
        assert single_array.length == 1
        assert single_array.values() == (555,)

        single_array.set(0, set_value)
        assert single_array.max_size == 1
        assert single_array.length == 1
        assert single_array.values() == (set_value,)

        self._set_scenario((1, 2, 3, 4, 5), 2, 100)
        self._set_scenario((1, 2, 3, 4, 5), 0, 100)
        self._set_scenario((1, 2, 3, 4, 5), 4, 100)
        self._set_scenario(("First", "Second", "Third", "Forth", "Fifth"), 2, "Hundred")

    def _set_scenario(self, values, index, replacement):
        many_array = SimpleArray(len(values))
        for value in values:
            many_array.add(value)

        many_array.set(index, replacement)
        assert many_array.values()[index] == replacement
        assert many_array.max_size == len(values)
        assert many_array.length == len(values)

    def test_insert(self):
        """
        Test array's insert operation
        :return:
        """
        insert_value = "A value"
        zero_array = SimpleArray(0)
        self.assertRaises(IndexError, zero_array.insert, -1, insert_value)
        self.assertRaises(IndexError, zero_array.insert, 0, insert_value)
        self.assertRaises(IndexError, zero_array.insert, 100, insert_value)

        single_array = SimpleArray(1)
        self.assertRaises(IndexError, single_array.insert, -1, insert_value)
        self.assertRaises(IndexError, single_array.set, 0, insert_value)
        self.assertRaises(IndexError, single_array.set, 1, insert_value)
        self.assertRaises(IndexError, single_array.insert, 100, insert_value)
        single_array.add("First")
        single_array.set(0, insert_value)
        assert single_array.max_size == 1
        assert single_array.length == 1
        assert single_array.values() == (insert_value,)

        self._insert_scenario((1, 2, 3, 4, 5), 0, 555, (555, 1, 2, 3, 4, 5))
        self._insert_scenario((1, 2, 3, 4, 5), 2, 555, (1, 2, 555, 3, 4, 5))
        self._insert_scenario((1, 2, 3, 4, 5), 4, 555, (1, 2, 3, 4, 555, 5))
        self._insert_scenario(("First", "Second", "Third", "Forth", "Fifth"), 2, "Hundred",
                              ("First", "Second", "Hundred", "Third", "Forth", "Fifth"))

    def _insert_scenario(self, values, insert_index, insert_value, test_result_value):
        many_array = SimpleArray(len(values) + 2)
        for value in values:
            many_array.add(value)

        many_array.insert(insert_index, insert_value)
        assert many_array.max_size == len(values) + 2
        assert many_array.length == len(values) + 1
        assert many_array.values() == test_result_value

        many_array.insert(many_array.length - 1, "Extra value")
        assert many_array.length == many_array.max_size

        with pytest.raises(OverflowError):
            many_array.insert(many_array.length - 1, "Super extra value")

    def test_delete(self):
        """
        Test array's delete operation
        :return:
        """
        zero_array = SimpleArray(0)
        self.assertRaises(IndexError, zero_array.delete, -1)
        self.assertRaises(IndexError, zero_array.delete, 0)
        self.assertRaises(IndexError, zero_array.delete, 100)

        single_array = SimpleArray(1)
        self.assertRaises(IndexError, single_array.delete, -1)
        self.assertRaises(IndexError, single_array.delete, 0)
        self.assertRaises(IndexError, single_array.delete, 1)
        self.assertRaises(IndexError, single_array.delete, 100)

        single_array.add("First")
        single_array.delete(0)
        assert single_array.max_size == 1
        assert single_array.length == 0
        assert single_array.values() == ()

        self._delete_scenario((1, 2, 3, 4, 5), 0, (2, 3, 4, 5))
        self._delete_scenario((1, 2, 3, 4, 5), 2, (1, 2, 4, 5))
        self._delete_scenario((1, 2, 3, 4, 5), 4, (1, 2, 3, 4))
        self._delete_scenario(("First", "Second", "Third", "Forth", "Fifth"), 2,
                              ("First", "Second", "Forth", "Fifth"))

    def _delete_scenario(self, values, index, test_values):
        many_array = SimpleArray(len(values))
        for value in values:
            many_array.add(value)
        many_array.delete(index)
        assert many_array.max_size == len(values)
        assert many_array.length == len(values) - 1
        assert many_array.values() == test_values

    def test_value_at(self):
        """
        Test array's value at index operation
        :return:
        """
        zero_array = SimpleArray(0)
        self.assertRaises(IndexError, zero_array.value_at, -1)
        self.assertRaises(IndexError, zero_array.value_at, 0)
        self.assertRaises(IndexError, zero_array.value_at, 100)

        single_array = SimpleArray(1)
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
        self._value_at_scenario(["First", "Second", "Third", "Forth", "Fifth", "Sixth"], 2,
                                "Third")

    def _value_at_scenario(self, values, index, text_value):
        many_array = SimpleArray(len(values))
        for value in values:
            many_array.add(value)

        assert many_array.max_size == len(values)
        assert many_array.length == len(values)
        assert many_array.value_at(index) == text_value
