import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Позитивные тесты

# Переводит первую букву в заглавную
def test_capitalize():
    assert string_utils.capitalize("тест") == "Тест"

# Делает все буквы строчными
def test_lower():
    assert string_utils.lower("Тест") == "тест"

# Делает все буквы заглавными
def test_upper():
    assert string_utils.upper("Тест") == "ТЕСТ"

# Убирает пробелы в начале
def test_trim():
    assert string_utils.trim("   04 апреля 2023") == "04 апреля 2023"

# Удаляет пробелы в начале и в конце
def test_strip():
    assert string_utils.strip("   04 апреля 2023   ") == "04 апреля 2023"

# Каждая буква в строке находится между запятыми и будет разделена на отдельные элементы списка
def test_to_list():
    assert string_utils.to_list("a,b,c,d", ",") == ["a", "b", "c", "d"]

# Удаляет указанный элемент слова
def test_to_delete_simbol():
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

# Проверяет начинается ли слово на этот символ True или False
def test_not_starts_with():
    assert string_utils.starts_with("Skypro", "y") == False

# Проверяет начинается ли слово на этот символ True или False
def test_to_starts_with():
    assert string_utils.starts_with("Skypro", "S") == True

# Негативные тесты

# Переводит первую букву в заглавную
def test_capitalize_empty_string():
    assert string_utils.capitalize("") == ""

# Делает все буквы строчными
def test_lower_empty_string():
    assert string_utils.lower("") == ""

# Убирает пробелы в начале
def test_trim_empty_string():
    assert string_utils.trim(" ") == ""

# Удаляет пробелы в начале и в конце
def test_strip_empty_string():
    assert string_utils.strip("     ") == ""
# Возвращает None
def test_capitalize_with_none():
    assert string_utils.capitalize(None) is None

# Проверяет поведение функции  delete_symbol из модуля  string_utils при передаче ей значения  None в качестве строки
def test_delete_symbol_with_none():
    assert string_utils.delete_symbol(None, 'a') is None

# Проверяет поведение функции  to_list из модуля  string_utils при передаче ей пустой строки
def test_to_list_empty_string():
    assert string_utils.to_list("") == []
