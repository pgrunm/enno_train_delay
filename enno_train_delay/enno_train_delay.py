import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class extract_train_delay_information:
    ''' 
    Class to extract train delay information from 
    the German railway company enno from https://der-enno.de.
    '''

    '''
    REGEX:
    1. Datum: ^\d{2}.\d{2}.\d{4}
    2. Uhrzeit: ^\d{2}.\d{2}.\d{4}\s(\d{2}:\d{2})
    3. Message: ^\d{2}.\d{2}.\d{4}\s\d{2}:\d{2}\s(.+)
    '''
    table_body_reg_expressions = [
        r'^\d{2}.\d{2}.\d{4}', r'^\d{2}.\d{2}.\d{4}\s(\d{2}:\d{2})', '^\d{2}.\d{2}.\d{4}\s\d{2}:\d{2}\s(.+)']

    def parse_train_delay_table(self, url):
        # Access the given URL and download the page
        firefox_options = Options()
        firefox_options.add_argument("--headless")

        # download Firefox Webdriver
        # https://github.com/mozilla/geckodriver/releases
        # put driver executable file in the script directory
        firefox_driver = os.path.join(os.getcwd(), "geckodriver")

        driver = webdriver.Firefox(
            firefox_options=firefox_options, executable_path=firefox_driver)

        # Download the URL's content
        driver.get(url)

        table = driver.find_element_by_id(id_='troubleTable')
        regex = re.compile(r'\n')
        table_text = regex.split(table.text)
        driver.close()
        return table_text

    def parse_train_delay_table_date(self, line):
        tr_reg_exp_date = re.compile(self.table_body_reg_expressions[0])

        # Extracting the Date
        date = tr_reg_exp_date.findall(line)
        return date[0]

    def parse_train_delay_table_time(self, line):
        tr_reg_exp_time = re.compile(self.table_body_reg_expressions[1])

        # Extracting the Time
        time = tr_reg_exp_time.findall(line)
        return time[0]

    def parse_train_delay_table_msg(self, line):
        tr_reg_exp_msg = re.compile(self.table_body_reg_expressions[2])

        # Extracting the message
        message = tr_reg_exp_msg.findall(line)
        return message[0]
