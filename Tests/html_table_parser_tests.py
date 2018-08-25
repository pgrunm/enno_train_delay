import unittest

import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from enno_train_delay import enno_train_delay

import re


class html_table_parser_tests(unittest.TestCase):
    '''
    to test:
    - extraction of table
    - extraction of table header
    - extraction of table body
    - extraction of table rows (date, time and message)
    '''

    test_url = 'https://www.der-enno.de/#meldungen'

    extracted_table_lines = ''

    def test_table_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        self.extracted_table_lines = parser.parse_train_delay_table(
            self.test_url)

        self.assertIsNotNone(self.extracted_table_lines)

    def test_header_is_in_first_line(self):
        print(self.extracted_table_lines)
        # self.assertIsInstance(header, str())
        # self.assertListEqual(header, ['Datum', 'Uhrzeit', 'Meldung'])


if __name__ == '__main__':
    unittest.main()
