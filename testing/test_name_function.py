import unittest

from get_formatted_name import get_formatted_name



class NamesTestCase(unittest.TestCase):
    """
    Здесь должно быть техническое задание
    которое должно выполнено
    функция должна принимать англ имена и возвращать их в корректном виде
    1. должны принимать с нижнего регистра и возвращать в верхнем
    2. должна принимать с пробелами и возвращать в нормальном виде
    3. должна корректно вызвращать с нижнего регистра с пробелами и с отчеством
    """
    def test_check_upper(self):
        """Работает ли коректно uppercase"""
        formated_name = get_formatted_name('semen', 'semenov')
        self.assertEqual(formated_name, "Semen Semenov")
    def test_check_whitespace(self):
        """ Работает ли корректно с пробелами"""
        formated_name = get_formatted_name('  semen ', '  semenov')
        self.assertEqual(formated_name, "Semen Semenov")
    def test_first_otch(self):
        """  Кейс 3"""
        formatted_name = get_formatted_name(' semen  ', ' semenich  ', ' semenov  ')
        self.assertEqual(formatted_name, 'Semen Semenich Semenov')

print(NamesTestCase.__doc__)
unittest.main()
