from typing import Union


class Search:
    """ Bisection efficient_algorithms — bisect module """
    @staticmethod
    def binary_search(numbers: list[int], item: int, sorted_numbers=False, start=0, end_index=None) -> Union[None, int]:
        """ Бинарный поиск: поиск индекса элемента в списке.
        Сложность — O(logn) при sorted_numbers == True
        Сложность — O(nlogn + logn) при sorted_numbers == False """
        if not sorted_numbers:
            numbers = sorted(numbers)
        if end_index is None:
            end_index = len(numbers) - 1
        # Пока не сузили список до одного элемента...
        while start <= end_index:
            # ... проверяем средний элемент
            mid = (start + end_index) // 2
            guess = numbers[mid]
            if guess == item:  # Значение найдено
                return mid
            if guess > item:  # Предположение было слишком высоким
                end_index = mid - 1
            else:  # Предположение было слишком низким
                start = mid + 1
        return None

    def insort_right(self, numbers: list[int], item: int, start=0, end=None, *, key=None) -> None:
        """ Вставьте элемент item в список numbers и сохраняйте его отсортированным, предполагая, что numbers отсортирован.
        Если item уже находится в numbers, вставьте его справа от самого правого item.
        Необязательные аргументы start (по умолчанию 0) и lenght (по умолчанию len(numbers)) привязывают
        фрагмент numbers для поиска.
        """
        if key is None:
            start = self.bisect_right(numbers, item, start, end)
        else:
            start = self.bisect_right(numbers, key(item), start, end, key=key)
        numbers.insert(start, item)

    def insort_left(self, numbers: list[int], item: int, start=0, end=None, *, key=None) -> None:
        """ Вставьте элемент item в список numbers и сохраняйте его отсортированным, предполагая, что numbers отсортирован.
        Если item уже находится в numbers, вставьте его слева от крайнего левого item.
        Необязательные аргументы start (по умолчанию 0) и lenght (по умолчанию len(numbers)) привязывают
        фрагмент numbers для поиска.
        """
        if key is None:
            start = self.bisect_left(numbers, item, start, end)
        else:
            start = self.bisect_left(numbers, key(item), start, end, key=key)
        numbers.insert(start, item)

    @staticmethod
    def bisect_right(numbers: list[int], item: int, start=0, end=None, *, key=None) -> int:
        """ Возвращает индекс для вставки элемента item в список numbers, предполагая, что numbers отсортирован.
        Возвращаемое значение i таково, что все e в numbers[:i] имеют e <= item,
        и все e в numbers[i:] имеет e > item. Таким образом, если item уже появляется в списке,
        numbers.insert(i, item) приведет вставьте сразу после крайнего правого item, который уже есть.
        Необязательные аргументы start (по умолчанию 0) и lenght (по умолчанию len(numbers)) привязывают
        фрагмент numbers для поиска.
        """
        if start < 0:
            raise ValueError('Начальное число отрицательное')
        if end is None:
            end = len(numbers)
        if key is None:
            while start < end:
                mid = (start + end) // 2
                if item < numbers[mid]:
                    end = mid
                else:
                    start = mid + 1
        else:
            while start < end:
                mid = (start + end) // 2
                if item < key(numbers[mid]):
                    end = mid
                else:
                    start = mid + 1
        return start

    @staticmethod
    def bisect_left(numbers: list[int], item: int, start=0, end=None, *, key=None) -> int:
        """ Возвращает индекс для вставки элемента item в список numbers, предполагая, что numbers отсортирован.
        Возвращаемое значение i такое, что все e в numbers[:i] имеют e < item,
        и все e в numbers[i:] имеет e >= x. Таким образом, если item уже появляется в списке,
        numbers.insert(i, item) приведет вставьте непосредственно перед крайним левым
        знаком x, который уже есть.
        Необязательные аргументы start (по умолчанию 0) и end (по умолчанию len(numbers)) привязывают
        фрагмент numbers для поиска.
        """
        if start < 0:
            raise ValueError('Начальное число отрицательное')
        if end is None:
            end = len(numbers)
        if key is None:
            while start < end:
                mid = (start + end) // 2
                if numbers[mid] < item:
                    start = mid + 1
                else:
                    end = mid
        else:
            while start < end:
                mid = (start + end) // 2
                if key(numbers[mid]) < item:
                    start = mid + 1
                else:
                    end = mid
        return start

    """ Ternary efficient_algorithms """

    def ternary_search(self, left: int, right: int, key: int, numbers: list[int]) -> int:
        """ Тернарный поиск. Сложность — O(log3n) """
        if right >= left:
            # Находим середину 1 (mid1) и середину 2 (mid2)
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            # Проверьте, равен ли ключ значению по середине
            if numbers[mid1] == key:
                return mid1
            if numbers[mid2] == key:
                return mid2

            # Поскольку ключ отсутствует в середине,
            # проверьте, в каком регионе он присутствует
            # затем повторите операцию поиска
            # в этом регионе
            if key < numbers[mid1]:
                # Ключ находится между левой частью списка и серединой 1 (mid1)
                return self.ternary_search(left, mid1 - 1, key, numbers)
            elif key > numbers[mid2]:
                # Ключ находится между серединой 2 (mid2) и правой частью списка
                return self.ternary_search(mid2 + 1, right, key, numbers)
            else:
                # Ключ находится где-то между серединой 1 (mid1) и серединой 2 (mid2)
                return self.ternary_search(mid1 + 1, mid2 - 1, key, numbers)
        return -1  # Ключ не найден
