"""
Задача:
Нужно написать реализацию функции `flat`, которая принимает список из `Item` и возвращает набор всех `id`, учитывая вложенность `item['children']`.
Порядок `id` в результате не важен.
"""


# обход графов в глубину


from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class Item:
    id: int
    name: str
    children: List["Item"]





def flat(items: List[Item]) -> Iterable[int]:
    result = set()
    for item in items:
        result.add(item.id)
        result.update(flat(item.children))
    return result



# Тестовый пример
test_items: List[Item] = [
    Item(
        id=1,
        name="1",
        children=[
            Item(
                id=2,
                name="2",
                children=[
                    Item(id=3, name="3", children=[]),
                    Item(id=4, name="4", children=[Item(id=9, name="8", children=[])]),
                ],
            ),
            Item(id=5, name="5", children=[]),
        ],
    ),
    Item(id=6, name="6", children=[]),
    Item(id=7, name="7", children=[Item(id=8, name="8", children=[])]),
]

result = set(flat(test_items))
# result = flat(test_items)
# print(result)
assert {1, 2, 3, 4, 5, 6, 7, 8, 9 } == result, f"expected: {result}"
print("result is OK")
