import re

import requests
from bs4 import BeautifulSoup


class extract_train_delay_information:

    '''
    Reg Expressions
    1. Datum: Gibt eine Liste mit Daten zurück
    2. Uhrzeit: Gibt eine Liste mit Uhrzeiten zurück
    3. Message: Gibt eine Liste mit Strings zurück
    '''
    table_body_reg_expressions = [
        '(\d{1,2}.\d{1,2}.\d{4})', '>(\d{1,2}:\d{1,2})<', '(\d{5}.+\.)']

    def parse_train_delay_table(self, url):
        # Access the given URL and download the page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and extract the Table with the ID troubleTable
        return soup.find(id='troubleTable')

    def parse_train_delay_table_header(self, table):
        soup = BeautifulSoup(table, 'html.parser')
        # Find the table header and extract it
        table_header = soup.find('thead')

        # Regular Expression: Capture everything with atleast 1 capital letter and unlimited lowercase letters
        th_reg_exp = re.compile('([A-Z]{1}[a-z]{1,})')
        return th_reg_exp.findall(str(table_header))

    def parse_train_delay_table_body(self, table):
        soup = BeautifulSoup(table, 'html.parser')

        # Getting the table body and returning it
        table_body = soup.find('tbody')
        return table_body

    def parse_train_delay_table_dates(self, table_body):
        tr_reg_exp_date = re.compile(self.table_body_reg_expressions[0])

        # Extracting the Dates
        dates = tr_reg_exp_date.findall(str(table_body))
        return dates

    def parse_train_delay_table_times(self, table_body):
        tr_reg_exp_time = re.compile(self.table_body_reg_expressions[1])

        # Extracting the Times
        times = tr_reg_exp_time.findall(str(table_body))
        return times

    def parse_train_delay_table_msg(self, table_body):
        tr_reg_exp_msg = re.compile(self.table_body_reg_expressions[2])

        # Extracting the Times
        messages = tr_reg_exp_msg.findall(str(table_body))
        return messages
