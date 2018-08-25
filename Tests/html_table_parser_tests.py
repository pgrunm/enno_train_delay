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

    def setUp(self):
        self.test_url = 'https://www.der-enno.de/#meldungen'
        parser = enno_train_delay.extract_train_delay_information()
        self.extracted_table_lines = parser.parse_train_delay_table(
            self.test_url)

        # Extracting the header and splitting it with a space as delimiter
        self.header = self.extracted_table_lines[0].split(' ')

        # Getting the table's content
        self.table_body = self.extracted_table_lines[1:]

    def test_table_extraction(self):
        # Returned text should not be empty
        self.assertIsNotNone(self.extracted_table_lines)

    def test_for_correct_instance_list(self):
        # Should return a list
        self.assertIsInstance(self.extracted_table_lines, list)

    def test_for_header(self):
        # Header should contain the items Datum, Uhrzeit and Meldung
        self.assertListEqual(self.header, ['Datum', 'Uhrzeit', 'Meldung'])

    def test_for_body(self):
        # Supposed to test the body rows...
        pass


if __name__ == '__main__':
    unittest.main()
