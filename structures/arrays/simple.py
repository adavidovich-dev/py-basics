"""
Simple array
"""


class SimpleArray:
    """
    Array with capacity implementation (C-like I suppose)
    """

    def __init__(self, size):
        if size < 0:
            raise ValueError("Array size must not be negative")
        self.__max_size = size
        self.__length = 0
        self.__array = [0] * self.__max_size

    def __str__(self):
        return str(self.__array)

    @property
    def max_size(self):
        """
        Array maximal capacity
        :return: max capacity
        """
        return self.__max_size

    @property
    def length(self):
        """
        Number of items in array
        :return: number of items
        """
        return self.__length

    def add(self, value):
        """
        Add element to the end of array
        :param value: value to add
        :return:
        """
        if self.__length + 1 > self.__max_size:
            raise OverflowError(f"Reached maximum of elements in ${self.__max_size} length array")
        self.__array[self.__length] = value
        self.__length = self.__length + 1

    def set(self, index, value):
        """
        Set value at specified index of array (replace element at index with value)
        :param index: index to set
        :param value: value to set
        :return:
        """
        if index < 0:
            raise IndexError(f"Index {index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index {index} out of range ${self.__length}")
        self.__array[index] = value

    def insert(self, index, value):
        """
        Insert value at specified index of array
        (insert value at specified index with moving of tail )
        :param index: index to insert
        :param value: value to insert
        :return:
        """
        if index < 0:
            raise IndexError(f"Index ${index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index ${index} out of range ${self.__length}")
        if self.__length + 1 > self.__max_size:
            raise OverflowError(f"Reached maximum of elements in ${self.__max_size} length array")
        for current_runner_index in range(self.__length - 1, index - 1, -1):
            self.__array[current_runner_index + 1] = self.__array[current_runner_index]
        self.__array[index] = value
        self.__length = self.__length + 1

    def delete(self, index):
        """
        Delete item with index from array
        :param index: index to delete
        :return:
        """
        if index < 0:
            raise IndexError(f"Index ${index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index ${index} out of range ${self.__length}")
        for current_runner_index in range(index, self.__length - 1):
            self.__array[current_runner_index] = self.__array[current_runner_index + 1]
        self.__length = self.__length - 1

    def value_at(self, index):
        """
        Return value at specified index of array
        :param index: index of item
        :return: value of item
        """
        if index < 0:
            raise IndexError(f"Index ${index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index ${index} out of range ${self.__length}")
        return self.__array[index]

    def linear_search(self, value):
        """
        Perform linear search of value in array
        :param value: value to search
        :return: index of found item value or -1
        """
        current_runner_index = 0
        while current_runner_index < self.__length:
            if self.__array[current_runner_index] == value:
                break
            current_runner_index = current_runner_index + 1
        if current_runner_index >= self.__length:
            return -1
        else:
            return current_runner_index

    def binary_search(self, value):
        """
        Perform binary search in array. It is supposed that array is sorted
        If array contains duplications then the most left element will be result of search
        :param value: value to search
        :return:  index of found item or -1
        """
        if self.__length == 0:
            return -1

        left_bound = 0
        right_bound = self.__length - 1
        while True:
            center = (left_bound + right_bound) // 2
            if self.__array[center] == value:
                found_element_index = center
                if found_element_index > 0:
                    while self.__array[found_element_index - 1] == self.__array[center]:
                        found_element_index = found_element_index - 1
                break
            if value < self.__array[center]:
                right_bound = center - 1
            else:
                left_bound = center + 1
            if left_bound > right_bound:
                found_element_index = -1
                break

        if found_element_index == -1:
            if self.linear_search(value) == -1:
                return -1
            else:
                raise RuntimeError("Binary search has been run on unsorted data")
        else:
            return found_element_index

    def values(self):
        """
        Return all values as list
        :return: values in array as list
        """
        return tuple(self.__array[i] for i in range(0, self.__length))

    def bubble_sort(self):
        """
        Perform bubble sort
        :return: nothing
        """
        for i_index in range(0, self.__length):
            for j_index in range(i_index + 1, self.__length):
                i_item = self.__array[i_index]
                j_item = self.__array[j_index]
                if i_item > j_item:
                    self.__array[j_index] = i_item
                    self.__array[i_index] = j_item

    def insert_sort(self):
        """
        Perform insert sort
        :return: nothing
        """
        if self.__length == 0:
            return
        for i_index in range(1, self.__length):
            selected = self.__array[i_index]
            j_index = i_index
            while j_index > 0 and self.__array[j_index - 1] > selected:
                self.__array[j_index] = self.__array[j_index - 1]
                j_index = j_index - 1
            self.__array[j_index] = selected

    def select_sort(self):
        """
        Perform select sort
        :return: nothing
        """
        for i_index in range(0, self.__length):
            i_item = self.__array[i_index]
            min_index = i_index
            for j_index in range(i_index + 1, self.__length):
                j_item = self.__array[j_index]
                if j_item < self.__array[min_index]:
                    min_index = j_index
            if min_index != i_index:
                self.__array[i_index] = self.__array[min_index]
                self.__array[min_index] = i_item
