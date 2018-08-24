from bs4 import BeautifulSoup
import re
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

soup = BeautifulSoup(html_string, 'html.parser')
# Extract the Table by ID
table = soup.find(id='troubleTable')
print(table)

# Find the table header and extract it
table_header = soup.find('thead')

# Regular Expression: Capture everything with atleast 1 capital letter and unlimited lowercase letters
th_reg_exp = re.compile('([A-Z]{1}[a-z]{1,})')
result = th_reg_exp.findall(str(table_header))

# Extracting the tbody
table_body = soup.findAll('tbody')
# print(table_body)

'''
Reg Expressions
1. Datum: Gibt eine Liste mit Daten zurück
2. Uhrzeit: Gibt eine Liste mit Uhrzeiten zurück
3. Message: Gibt eine Liste mit Strings zurück
'''
table_body_reg_expressions = [
    '(\d{1,2}.\d{1,2}.\d{4})', '>(\d{1,2}:\d{1,2})<', '(\d{5}.+\.)']
