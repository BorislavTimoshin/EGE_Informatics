import collections
import math
from typing import Union
from sorting_algorithms import Sorting
from search_algorithms import Search
from graph_algorithms import Graph


class Algorithms(Sorting, Search, Graph):
    @staticmethod
    def conversion_to_number_system(number: int, base: int) -> str:
        """ Перевод числа в заданную систему счисления """
        result = ''
        while number > 0:
            number, d = divmod(number, base)
            sd = str(d) if d < 10 else chr(ord('A') + d - 10)
            result = sd + result
        return result

    @staticmethod
    def decimal_conversion(string_of_numbers: str, base: int) -> int:
        """ Перевод из любой системы счисления в десятичную """
        result = 0
        for index in map(ord, string_of_numbers):
            if index < ord('A'):
                d = index - ord('0')
            else:
                d = index - ord('A') + 10
            result = result * base + d
        return result

    @staticmethod
    def sieve_of_eratosthenes(number: int) -> list[int]:
        """ Решето Эратосфена — нахождение всех простых чисел от 1 до целого числа n """
        prime = [True] * (number + 1)
        p = 2
        while p * p <= number:
            if prime[p] is True:
                for i in range(p * p, number + 1, p):
                    prime[i] = False
            p += 1
        return [x for x in range(2, number + 1) if prime[x]]

    @staticmethod
    def get_divisors_fast(number: int) -> list[int]:
        """
        Получение списка делителей числа. Сложность — O(n ** 0.5)
        Используется sqrt() из модуля math
        Используется двусвязанный список deque() из библиотеки collections
        для добавления элементов с обеих сторон со сложностью O(1).
        Иначе сложность добавления элементов в обычный список будет O(n) """
        nsqrt = math.sqrt(number)
        divisors = collections.deque()
        if nsqrt.is_integer():
            divisors.append(int(nsqrt))
        for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
            if number % i == 0:
                divisors.appendleft(i)
                divisors.append(number // i)
        return list(divisors)

    @staticmethod
    def get_count_divisors_fast(number: int) -> int:
        """ Получение количества делителей числа. Сложность — O(n ** 0.5)
        Используется sqrt() из модуля math """
        nsqrt = math.sqrt(number)
        count = 0
        if nsqrt.is_integer():
            count = 1
        for i in range(int(nsqrt) - nsqrt.is_integer(), 0, -1):
            if number % i == 0:
                count += 2
        return count

    @staticmethod
    def min_divisor_option_1(number: int) -> int:
        """ Нахождение минимального делителя. Сложность O(1) для четных чисел и для нечетных чисел в диапазоне [1, 9]
        Сложность — O((n ** 0.5) // 2) для остальных нечетных чисел """
        if number % 2 == 0:
            return 2  # обработка чётных чисел
        nsqrt = int(math.sqrt(number))
        for i in range(3, nsqrt + 1, 2):
            if number % i == 0:
                return i
        return number

    @staticmethod
    def min_divisor_option_2(number: int) -> int:
        """ Нахождение минимального делителя. Сложность O(1) для четных чисел и для нечетных чисел в диапазоне [1, 9]
        Сложность — O((n ** 0.5) // 2) для остальных нечетных чисел """
        if number % 2 == 0:
            return 2  # обработка чётных чисел
        # q - итеративно накапливает значения квадратов нечётных чисел
        # s - арифметическая прогрессия с шагом 8
        i, q, s = 3, 9, 8
        while q <= number:
            if number % i == 0:
                return i
            i += 2
            s += 8
            q += s
        return number

    @staticmethod
    def is_prime(number: int) -> bool:
        """ Проверка на простоту числа. Сложность — O(1) для четных чисел и для числа 1.
        Сложность — O((n ** 0.5) // 2) для остальных нечетных чисел """
        if number == 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        nsqrt = int(math.sqrt(number))
        for i in range(3, nsqrt + 1, 2):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def factorize(number: int) -> list[int]:
        """ Разложение числа на простые множители. Сложность — O(n ** 0.5 + logn) = O(n ** 0.5)
         Используется двусвязанный список deque() из библиотеки collections
        для добавления элементов с обеих сторон со сложностью O(1). """
        factors = collections.deque([1])
        nsqrt = int(math.sqrt(number))
        while number % 2 == 0:
            factors.append(2)
            number //= 2
        for i in range(3, int(nsqrt ** 0.5) + 1, 2):
            while number % i == 0:
                factors.append(i)
                number //= i
        if number > 1:
            factors.append(number)
        return list(factors)

    @staticmethod
    def amount_pairs_with_difference_greater_k(numbers: list[int], k: int, lenght=None, sorted_numbers=False) -> int:
        """ Используется метод двух указателей. Сложность — O(2n) при отсортированном списке numbers, то есть
        sorted_numbers == True. Сложность — O(nlogn + 2n) при неотсортированном списке numbers, то есть
        sorted_numbers == False. """
        if not sorted_numbers:
            numbers = sorted(numbers)
        if lenght is None:
            lenght = len(numbers)
        second = 0
        amount = 0
        for first in range(lenght):
            while second != lenght and numbers[second] - numbers[first] <= k:
                second += 1
            amount += lenght - second
        return amount

    @staticmethod
    def max_product_of_k_numbers_from_n(n: int, k: int, numbers: list[int, float]) -> Union[float, int]:
        """ Найти K чисел последовательности, произведение которых максимально.
        Сложность — O(nlogn + k). Числа последовательности могут быть отрицательными """
        result = 1
        numbers = sorted(numbers)
        if numbers[0] >= 0:
            for i in range(n - 1, n - k - 1, -1):
                result *= numbers[i]
        elif numbers[-1] <= 0:
            if k % 2 == 0:
                for i in range(k):
                    result *= numbers[i]
            else:
                for i in range(n - 1, n - k - 1, -1):
                    result *= numbers[i]
        else:
            left = 0
            right = n - 1
            while k > 0:
                mult = numbers[left] * numbers[left + 1]
                if k > 1 and mult >= numbers[right] * numbers[right - 1]:
                    result *= mult
                    left += 2
                    k -= 2
                else:
                    result *= numbers[right]
                    right -= 1
                    k -= 1
        return result

    @staticmethod
    def two_sum(numbers: list[int], target: int) -> Union[None, tuple[int, int]]:
        """ Находим 2 элемента, сумма которых должна равняться target, с помощью метода двух указателей. Сложность — O(n) """
        # Инициализируем переменные left и right, которые будут использоваться для поиска суммы двух чисел, равной target
        left, right = 0, len(numbers) - 1
        # Пока указатель left меньше указателя right
        while left < right:
            # Вычисляем сумму двух чисел, находящихся по указателям left и right
            summa = numbers[left] + numbers[right]
            # Если сумма равна целевому числу target, возвращаем список из двух чисел
            if summa == target:
                return numbers[left], numbers[right]
            # Если сумма меньше целевого числа target, увеличиваем указатель left на 1
            elif summa < target:
                left += 1
            # Если сумма больше целевого числа target, уменьшаем указатель right на 1
            else:
                right -= 1
        return  # Если не найдено двух чисел, сумма которых равна целевому числу target, возвращаем None

    @staticmethod
    def euler_function(number):
        """ Функция Эйлера: нахождение количества чисел от 1 до number, взаимно простых с number. Иными словами, это
        количество таких чисел в отрезке [1; number], наибольший общий делитель которых с number равен единице.
        Сложность O(n ** 0.5) """
        result = number
        i = 2
        while i * i <= number:
            if number % i == 0:
                while number % i == 0:
                    number //= i
                result -= result // i
            i += 1
        if number > 1:
            result -= result // number
        return result

    def gcd_recursion(self, a: int, b: int) -> int:
        """ Нахождение наибольшего общего делителя (greatest common divisor) рекурсивно
         Но есть и функция gcd в модуле math и не только. Сложность O(log(min(a, b))) """
        if b == 0:
            return a
        return self.gcd_recursion(b, a % b)

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """ Нахождение наибольшего общего делителя (greatest common divisor)
         Но есть и функция gcd в модуле math и не только. Сложность O(log(min(a, b))) """
        while b:
            a, b = b, a % b
        return a

    def gcd_advanced(self, a, b) -> tuple[int, int, int]:
        """ В то время как "обычный" алгоритм Евклида просто находит наибольший общий делитель двух чисел a и b,
        расширенный алгоритм Евклида находит помимо НОД также коэффициенты x и y такие, что:
        a * x + b * y = gcd(a, b)
        Т.е. он находит коэффициенты, с помощью которых НОД двух чисел выражается через сами эти числа.
        Расширенный алгоритм Евклида в такой реализации работает корректно даже для отрицательных чисел. """
        if a == 0:
            return b, 0, 1
        d, x1, y1 = self.gcd_advanced(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return d, x, y

    def lcm(self, a: int, b: int) -> int:
        """ Нахождение наименьшего общего кратного (least common multiplier) Сложность O(log(min(a, b))) """
        return (a * b) // self.gcd(a, b)

    @staticmethod
    def fact_pow(n: int, k: int) -> int:
        """ Нахождение наибольшего x, такого, что n! делится на k ** x. Сложность O(logk(n)) """
        result = 0
        while n:
            n //= k
            result += n
        return result


# NFS
algorithm = Algorithms()
