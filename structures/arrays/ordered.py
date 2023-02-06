"""
Ordered array
"""


class OrderedArray:
    """
       Ordered array with capacity implementation
    """

    def __init__(self, size):
        if size < 0:
            raise ValueError("Array size must not be negative")
        self.__max_size = size
        self.__length = 0
        self.__array = [0] * self.__max_size

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
        Add element to the array
        :param value: value to add
        :return:
        """
        if self.__length + 1 > self.__max_size:
            raise OverflowError(f"Reached maximum of elements in ${self.__max_size} length array")

        insert_index = 0
        while insert_index < self.__length:
            if value < self.__array[insert_index]:
                break
            insert_index += 1

        for runner in range(self.__length, insert_index, -1):
            self.__array[runner] = self.__array[runner - 1]
        self.__array[insert_index] = value
        self.__length += 1

    def delete(self, value):
        """
        Delete item with index from array
        :param value: value to delete
        :return:
        """
        index_to_delete = self.find(value)
        if index_to_delete != -1:
            for runner_index in range(index_to_delete, self.__length - 1):
                self.__array[runner_index] = self.__array[runner_index + 1]
            self.__length = self.__length - 1

    def index_of(self, value):
        """
        Index of element in array
        :param value: value to search
        :return: element's index or -1
        """
        return self.find(value)

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

    def find(self, value):
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
            if value == self.__array[center]:
                found_element_index = center
                if found_element_index > 0:
                    while self.__array[found_element_index - 1] == self.__array[center]:
                        found_element_index -= 1
                break
            if value < self.__array[center]:
                right_bound = center - 1
            else:
                left_bound = center + 1
            if left_bound > right_bound:
                found_element_index = -1
                break
        return found_element_index

    def values(self):
        """
        Return all values as list
        :return: values in array as list
        """
        return tuple(self.__array[i] for i in range(0, self.__length))
