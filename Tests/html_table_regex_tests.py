import re
import unittest

from bs4 import BeautifulSoup


class RegExTests(unittest.TestCase):

    html_string = """<table class="troubletable" id="troubleTable">
				<thead>
					<tr>
						<td style="width: 180px;">Datum</td>
						<td style="width: 100px;">Uhrzeit</td>
						<td class="tal">Meldung</td>
					</tr>
				</thead>
				<tbody>
                <tr class="append"><td class="">23.08.2018</td><td class="start">21:11</td><td class="tal pl10 message">83533 Hannover Hbf → Wolfsburg hat in Dedenhausen (planmäßig 21:11) +14 min. Grund: Schäden an den Gleisanlagen.</td></tr>
                <tr class="append"><td class="">23.08.2018</td><td class="start">21:01</td><td class="tal pl10 message">83530 Wolfsburg → Hannover Hbf hat in Lehrte (planmäßig 21:01) +25 min. Grund: Schäden an den Gleisanlagen.</td></tr>
                <tr class="append"><td class="">23.08.2018</td><td class="start">20:43</td><td class="tal pl10 message">83531 Hannover Hbf → Wolfsburg hat in Wolfsburg (planmäßig 20:43) +13 min. Grund: Schäden an den Gleisanlagen.</td></tr>
                </tbody>
				<tfoot>
					<tr>
						<td colspan="6" class="trouble-no-message" style="display: none;">Zur Zeit sind keine Meldungen vorhanden.</td>
					</tr>
				</tfoot>
			</table>
    """

    # List of regular expressions
    table_body_reg_expressions = [
        '(\d{1,2}.\d{1,2}.\d{4})', '>(\d{1,2}:\d{1,2})<', '(\d{5}.+\.)']

    def test_reg_ex_table_header(self):
        soup = BeautifulSoup(self.html_string, 'html.parser')
        # Getting the table header
        table_header = soup.find('thead')
        th_reg_exp = re.compile('([A-Z]{1}[a-z]{1,})')
        # Extracting the Table Header
        result = th_reg_exp.findall(str(table_header))

        # Checking the Table Header
        # Should be a list
        self.assertIsInstance(result, list)
        # Should contain the following items
        self.assertListEqual(result, ['Datum', 'Uhrzeit', 'Meldung'])

    def test_reg_ex_table_row_date(self):
        soup = BeautifulSoup(self.html_string, 'html.parser')

        # Getting the table header
        table_body = soup.find('tbody')
        tr_reg_exp_date = re.compile(self.table_body_reg_expressions[0])

        # Extracting the Table Header
        result = tr_reg_exp_date.findall(str(table_body))

        # Checking the Table Header
        # Should be a list
        self.assertIsInstance(result, list)

        # Should contain the following items
        self.assertListEqual(
            result, ['23.08.2018', '23.08.2018', '23.08.2018'])

    def test_reg_ex_table_row_time(self):
        soup = BeautifulSoup(self.html_string, 'html.parser')

        # Getting the table header
        table_body = soup.find('tbody')
        tr_reg_exp_time = re.compile(self.table_body_reg_expressions[1])

        # Extracting the Table Header
        result = tr_reg_exp_time.findall(str(table_body))

        # Checking the Table Header
        # Should be a list
        self.assertIsInstance(result, list)

        # Should contain the following items
        self.assertListEqual(
            result, ['21:11', '21:01', '20:43'])

    def test_reg_ex_table_row_msg(self):
        soup = BeautifulSoup(self.html_string, 'html.parser')

        # Getting the table header
        table_body = soup.find('tbody')
        tr_reg_exp_msg = re.compile(self.table_body_reg_expressions[2])

        # Extracting the Table Header
        result = tr_reg_exp_msg.findall(str(table_body))

        # Checking the Table Header
        # Should be a list
        self.assertIsInstance(result, list)

        # Should contain the following items
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
