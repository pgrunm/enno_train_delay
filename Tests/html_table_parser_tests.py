import unittest

import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from enno_train_delay import enno_train_delay


class html_table_parser_tests(unittest.TestCase):
    '''
    to test:
    - extraction of table
    - extraction of table header
    - extraction of table body
    - extraction of table rows (date, time and message)
    '''

    test_url = 'https://www.der-enno.de/#meldungen'

    extracted_table = ''
    extracted_table_header = ''
    extracted_table_body = ''

    def test_table_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        self.extracted_table = parser.parse_train_delay_table(self.test_url)

        self.assertIsNotNone(self.extracted_table)

    def test_table_header_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        self.extracted_table_header = parser.parse_train_delay_table_header(
            self.extracted_table)

        # Extracted table head should contain the following columns
        self.assertListEqual(self.extracted_table_header, [
                             'Datum', 'Uhrzeit', 'Meldung'])

    def test_table_body_row_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()

        # Extracting the table body
        self.extracted_table_body = parser.parse_train_delay_table_body(
            self.extracted_table)

        self.assertIsNotNone(self.extracted_table_body)

    def test_table_row_date_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        rows = parser.parse_train_delay_table_dates(self.extracted_table_body)

        self.assertIsNotNone(rows)

    def test_table_row_time_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        rows = parser.parse_train_delay_table_times(self.extracted_table_body)

        self.assertIsNotNone(rows)

    def test_table_row_msg_extraction(self):
        parser = enno_train_delay.extract_train_delay_information()
        rows = parser.parse_train_delay_table_msg(self.extracted_table_body)

        self.assertIsNotNone(rows)


if __name__ == '__main__':
    unittest.main()
