import unittest

from main import ATM

class TestATM(unittest.TestCase):
    """
    Запуск из командной строки:
    python3 -m unittest test_atm.py
    """
    def setUp(self):
        self.atm = ATM()

    def test_deposit_correct_length(self):
        """
        Проверяет, что метод deposit корректно обновляет количество банкнот, 
        если длина списка равна 5.
        """
        self.atm.deposit([1, 1, 1, 1, 1])
        self.assertEqual(self.atm.container_banknotes, [1, 1, 1, 1, 1])

    def test_deposit_incorrect_length(self):
        """
        Проверяет, что метод deposit вызывает ошибку, 
        если длина списка не равна 5.
        """
        with self.assertRaises(IndexError):
            self.atm.deposit([1, 1, 1, 1])

    def test_deposit_large_values(self):
        """
        Проверяет, что метод deposit корректно обрабатывает большие значения, 
        до $10^9$.
        """
        self.atm.deposit([10**9, 10**9, 10**9, 10**9, 10**9])
        self.assertEqual(self.atm.container_banknotes, 
                         [10**9, 10**9, 10**9, 10**9, 10**9])

    def test_withdraw_amount_too_large(self):
        """
        Проверяет, что метод withdraw возвращает [-1], 
        если запрашиваемая сумма больше $10^9$.
        """
        result = self.atm.withdraw(10**9 + 1)
        self.assertEqual(result, [-1])

    def test_withdraw_successful(self):
        """
        Проверяет, что метод withdraw корректно работает, если снятие возможно.
        """
        self.atm.deposit([0, 0, 1, 2, 1])
        result = self.atm.withdraw(600)
        self.assertEqual(result, [0, 0, 1, 0, 1])

    def test_withdraw_not_possible(self):
        """
        Проверяет, что метод withdraw возвращает [-1], если снятие невозможно.
        """
        self.atm.deposit([0, 0, 1, 2, 1])
        result = self.atm.withdraw(1100)  # Should not be possible
        self.assertEqual(result, [-1])

    def test_withdraw_exact_amount(self):
        """
        Проверяет, что метод withdraw корректно работает, 
        если запрашиваемая сумма равна одному из номиналов.
        """
        self.atm.deposit([0, 0, 1, 2, 1])
        result = self.atm.withdraw(500)
        self.assertEqual(result, [0, 0, 0, 0, 1])

    def test_withdraw_edge_cases(self):
        """
        Проверяет случаи, когда сумма меньше минимального номинала 
        или произвольное большое значение.
        """
        self.atm.deposit([1, 1, 1, 1, 1])
        result = self.atm.withdraw(1)
        self.assertEqual(result, [-1])
        
        result = self.atm.withdraw(123456789)
        self.assertEqual(result, [-1])


if __name__ == '__main__':
    unittest.main()
