class Sorting:
    @staticmethod
    def bubble_sort(numbers: list, lenght=None) -> list:
        """ Сортировка пузырьком. Список может иметь любые объекты, которые можно сравнить. Сложность — O(n ** 2) """
        if lenght is None:
            lenght = len(numbers)
        for i in range(lenght):
            for j in range(lenght - i - 1):  # Проходимся по всем элементам, кроме отсортированных
                if numbers[j] > numbers[j + 1]:  # Сравниваем элемент по следующим
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Меняем местами, если следующий меньше
        return numbers

    @staticmethod
    def selection_sort(numbers: list, lenght=None) -> list:
        """ Сортировка выбором. Список может иметь любые объекты, которые можно сравнить. Сложность — O(n ** 2) """
        if lenght is None:
            lenght = len(numbers)
        for i in range(lenght - 1):
            smallest = i
            for j in range(i + 1, lenght):
                if numbers[j] < numbers[smallest]:
                    smallest = j
            numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
        return numbers

    @staticmethod
    def insertion_sort(numbers: list, lenght=None) -> list:
        """ Сортировка вставками. Список может иметь любые объекты, которые можно сравнить.
        Сложность — O(n ** 2). В лучшем случае, если список отсортирован, сложность равна O(n) """
        if lenght is None:
            lenght = len(numbers)
        for i in range(1, lenght):
            temp = numbers[i]
            j = i - 1
            while j >= 0 and temp < numbers[j]:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = temp
        return numbers

    @staticmethod
    def counting_sort(numbers: list[int], minval=None, maxval=None) -> list[int]:
        """ Сортировка подсчетом. Сложность — O(n + k) """
        if minval is None:
            minval = min(numbers)
        if maxval is None:
            maxval = max(numbers)
        k = maxval - minval + 1
        count = [0] * k
        for number in numbers:
            count[number - minval] += 1
        now_pos = 0
        for val in range(k):
            for i in range(count[val]):
                numbers[now_pos] = val + minval
                now_pos += 1
        return numbers

    def merge_sort(self, numbers: list[int]) -> list[int]:
        """ Сортировка слиянием. Сложность — O(nlogn) """
        len_numbers = len(numbers)
        if len_numbers > 1:
            middle = len_numbers // 2
            left = numbers[:middle]
            right = numbers[middle:]
            self.merge_sort(left)
            self.merge_sort(right)
            len_left = len(left)
            len_right = len(right)
            # Используем метод двух указателей для слияния:
            i = j = k = 0
            while i < len_left and j < len_right:
                if left[i] < right[j]:
                    numbers[k] = left[i]
                    i += 1
                else:
                    numbers[k] = right[j]
                    j += 1
                k += 1
            while i < len_left:
                numbers[k] = left[i]
                i += 1
                k += 1
            while j < len_right:
                numbers[k] = right[j]
                j += 1
                k += 1
        return numbers

    def quick_sort(self, numbers: list[int]) -> list[int]:
        """ Быстрая сортировка. Сложность — O(nlogn) """
        if len(numbers) < 2:  # Если длина списка меньше 2, он уже отсортирован
            return numbers
        pivot = numbers[0]  # Выбираем опорный элемент (обычно это первый или последний элемент)
        # Создаём пустые списки для элементов меньше и больше опорного элемента
        less = []
        greater = []
        # Итерируемся по списку и добавляем элементы в соответствующие списки
        for element in numbers[1:]:
            if element <= pivot:
                less.append(element)
            else:
                greater.append(element)
        # Рекурсивно вызываем быструю сортировку для каждого из списков
        # и объединяем результаты вместе с опорным элементом
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)
