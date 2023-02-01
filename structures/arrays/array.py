class Array:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Array size must not be negative")
        self.__max_size = size
        self.__length = 0
        self.__array = [0] * self.__max_size

    @property
    def max_size(self):
        return self.__max_size

    @property
    def length(self):
        return self.__length

    def add(self, value):
        if self.__length + 1 > self.__max_size:
            raise OverflowError(f"Reached maximum of elements in ${self.__max_size} length array")
        self.__array[self.__length] = value
        self.__length = self.__length + 1

    def set(self, index, value):
        if index < 0:
            raise IndexError(f"Index {index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index {index} out of range ${self.__length}")
        self.__array[index] = value

    def insert(self, index, value):
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
        if index < 0:
            raise IndexError(f"Index ${index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index ${index} out of range ${self.__length}")
        for current_runner_index in range(index, self.__length - 1):
            self.__array[current_runner_index] = self.__array[current_runner_index + 1]
        self.__length = self.__length - 1

    def value_at(self, index):
        if index < 0:
            raise IndexError(f"Index ${index} is negative")
        if index >= self.__length:
            raise IndexError(f"Index ${index} out of range ${self.__length}")
        return self.__array[index]

    def linear_search(self, value):
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
        left_bound = 0
        right_bound = self.__length - 1
        while True:
            center = (left_bound + right_bound) // 2
            if self.__array[center] == value:
                found_element_index = center
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
        return self.__array[0: self.__length]
