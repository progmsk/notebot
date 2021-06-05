import unittest
from bot_handler import Handler
from convert import *

class TestStringMethods(unittest.TestCase):
    def init(self):
        self.head = Handler(None)

        self.list_to_test = {
            '  3 from 10 to 2': '11',
            '3from 10 to 2': '11',
            '121 from 3to 8': '20',
            '3123 from 4 to8': '333',
            '3123 from 4 to 5': '1334',
            'A2 from 16 to 2': '10100010',
        }
        self.list_to_bin = {
            '3': '11',
            ' 4': '100',
            '5 ': '101',
            '77': '1001101',
        }
        self.list_to_bin_2 = {
            '13from8': '1011',
            ' 43from8': '100011',
            '56 from 16 ': '1010110',
            'A2from16': '10100010',
        }
        self.list_to_all_minus = {
            '-A1from16': '-10100001',
            ' -43from8': '-100011',
            '-56 from 16 ': '-1010110',
            '-A2from16': '-10100010',
        }

    def test_convert_all(self):
        self.init()
        self.assertEqual('11', convert_by_norminate(3, 10, 2))
        self.assertEqual('11', convert_by_norminate(3, 10, 2))
        for item in self.list_to_test:
            #print(f'___{self.list_to_test[item]} | {self.head.make(item)}')
            #self.assertEqual(self.list_to_test[item], self.head.make(item))
            self.assertEqual(self.list_to_test[item], convert_from_text(item))

    def test_convert_to_bin(self):
        self.init()
        for item in self.list_to_bin:
            #self.assertEqual(self.list_to_bin[item], self.head.make(item))
            self.assertEqual(self.list_to_bin[item], convert_from_text(item))

    def test_convert_to_bin_2(self):
        self.init()
        for item in self.list_to_bin_2:
            #self.assertEqual(self.list_to_bin_2[item], self.head.make(item))
            self.assertEqual(self.list_to_bin_2[item], convert_from_text(item))

    def test_convert_to_all_minus(self):
        self.init()
        for item in self.list_to_all_minus:
            self.assertEqual(self.list_to_all_minus[item], convert_from_text(item))
            #self.assertEqual(self.list_to_all_minus[item], self.head.make(item))

if __name__ == '__main__':
    unittest.main()
