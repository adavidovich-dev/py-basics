class SearchUnitData:
    def __init__(self, a_list, value, index):
        self.list = a_list
        self.value = value
        self.index = index


class AddUnitData:
    def __init__(self, a_list, add_value, check_list):
        self.list = a_list
        self.add_value = add_value
        self.check_list = check_list


search_sorted_data = [
    SearchUnitData((), 0, -1),
    SearchUnitData((1,), -1, -1),
    SearchUnitData((1,), 1, 0),
    SearchUnitData((1, 2, 3, 4, 5), -1, -1),
    SearchUnitData((1, 2, 3, 4, 5), 1, 0),
    SearchUnitData((1, 2, 3, 4, 5), 3, 2),
    SearchUnitData((1, 2, 3, 4, 5), 5, 4),
    SearchUnitData((1, 2, 3, 4, 5, 6), -1, -1),
    SearchUnitData((1, 2, 3, 4, 5, 6), 1, 0),
    SearchUnitData((1, 2, 3, 4, 5, 6), 4, 3),
    SearchUnitData((1, 2, 3, 4, 5, 6), 6, 5),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5), -1, -1),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5), 1, 0),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5), 3, 4),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5), 5, 8),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6), -1, -1),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6), 1, 0),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6), 4, 6),
    SearchUnitData((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6), 6, 10),
    SearchUnitData(range(1, 1_000), -1, -1),
    SearchUnitData(range(1, 1_000), 1, 0),
    SearchUnitData(range(1, 1_000), 444, 443),
    SearchUnitData(range(1, 1_000), 999, 998)
]

search_unsorted_data = [SearchUnitData((5, 2, 4, 3, 1), -1, -1),
                        SearchUnitData((5, 2, 4, 3, 1), 5, 0),
                        SearchUnitData((5, 2, 4, 3, 1), 4, 2),
                        SearchUnitData((5, 2, 4, 3, 1), 1, 4),
                        SearchUnitData((5, 2, 4, 3, 6, 1), -1, -1),
                        SearchUnitData((5, 2, 4, 3, 6, 1), 5, 0),
                        SearchUnitData((5, 2, 4, 3, 6, 1), 3, 3),
                        SearchUnitData((5, 2, 4, 3, 6, 1), 1, 5)]

add_sorted_data = [
    AddUnitData((), 1, (1,)),
    AddUnitData((1, 2), 1, (1, 1, 2)),
    AddUnitData((1, 1, 1, 2), 1, (1, 1, 1, 1, 2)),
    AddUnitData((1,), 2, (1, 2)),
    AddUnitData((1, 2), 2, (1, 2, 2)),
    AddUnitData((1, 2, 2), 2, (1, 2, 2, 2)),
    AddUnitData((1, 2, 4), 3, (1, 2, 3, 4)),
    AddUnitData((1, 2, 3), 4, (1, 2, 3, 4)),
    AddUnitData((1, 2, 2, 4), 3, (1, 2, 2, 3, 4)),
    AddUnitData((1, 2, 3, 3), 4, (1, 2, 3, 3, 4)),

    AddUnitData((100, 200, 300, 400), 50, (50, 100, 200, 300, 400)),
    AddUnitData((100, 200, 300, 400), 250, (100, 200, 250, 300, 400)),
    AddUnitData((100, 200, 300, 400), 450, (100, 200, 300, 400, 450)),

    AddUnitData(("a", "b", "c", "e", "f", "g"), "d", ("a", "b", "c", "d", "e", "f", "g"))
]

sort_data = [
    {'array': (), 'test': ()},
    {'array': (1,), 'test': (1,)},
    {'array': (1, 2), 'test': (1, 2)},
    {'array': (2, 1), 'test': (1, 2)},
    {'array': (3, 2, 1), 'test': (1, 2, 3)},
    {'array': (4, 3, 2, 1), 'test': (1, 2, 3, 4)},
    {'array': (1, 3, 2), 'test': (1, 2, 3)},
    {'array': (1, 3, 2, 4), 'test': (1, 2, 3, 4)},
    {'array': (2, 1, 7, 5, 3, 6, 8), 'test': (1, 2, 3, 5, 6, 7, 8)},
    {'array': (2, 2), 'test': (2, 2)},
    {'array': (3, 3, 3), 'test': (3, 3, 3)},
    {'array': (1, 3, 3, 2), 'test': (1, 2, 3, 3)},
    {'array': (1, 2, 3, 5, 4, 4), 'test': (1, 2, 3, 4, 4, 5)},
    {'array': range(1, 1_000), 'test': range(1, 1_000)},
]
