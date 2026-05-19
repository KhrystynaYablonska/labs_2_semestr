import os
import sys
import unittest

# Додаємо папку src до шляху пошуку модулів, щоб unittest міг імпортувати kmp
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from kmp import kmp_search


class TestKMPSearch(unittest.TestCase):

    def test_multiple_occurrences(self):
        """Тест для кількох окремих входжень підстрічки."""
        self.assertEqual(kmp_search("abababab", "ab"), [0, 2, 4, 6])

    def test_single_occurrence(self):
        """Тест для одного входження всередині рядка."""
        self.assertEqual(kmp_search("hello world", "world"), [6])

    def test_no_occurrence(self):
        """Тест, коли шуканого рядка немає в тексті."""
        self.assertEqual(kmp_search("abcdefg", "xyz"), [])

    def test_overlapping_occurrences(self):
        """Тест для входжень, які частково перекривають одне одного."""
        self.assertEqual(kmp_search("aaaaa", "aaa"), [0, 1, 2])

    def test_empty_needle(self):
        """Тест із порожнім шуканим рядком."""
        self.assertEqual(kmp_search("haystack", ""), [])

    def test_empty_haystack(self):
        """Тест із порожнім основним текстом."""
        self.assertEqual(kmp_search("", "needle"), [])

    def test_needle_longer_than_haystack(self):
        """Тест, коли шуканий рядок довший за сам текст."""
        self.assertEqual(kmp_search("short", "longer_needle"), [])


if __name__ == "__main__":
    unittest.main()