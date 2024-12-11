import unittest
import regular_expressions

# Датасет для тестов
with open('data.txt', 'r') as f:
    test_cases = [list(map(str, line.split(','))) for line in f]

for x in range(len(test_cases)):
    test_cases[x][1] = True if test_cases[x][1] == '1\n' else False 

# Класс для тестирования функции
class TestIsValidPostcode(unittest.TestCase):

    def test_postcodes(self):
        for postcode, expected in test_cases:
            with self.subTest(postcode=postcode):
                self.assertEqual(regular_expressions.is_valid_postcode(postcode), expected)


if __name__ == '__main__':
    choice = int(input("Ввести вручную - 0 \
                        \nОбработать тесты - 1 \n"))
    if choice:
        unittest.main()
    else:
        index = input("Введите индекс ")
        print(regular_expressions.is_valid_postcode(index))
