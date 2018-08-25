from enno_train_delay import enno_train_delay

url = 'https://www.der-enno.de/#meldungen'

parser = enno_train_delay.extract_train_delay_information()

# Retrieve the table
table = parser.parse_train_delay_table(url)

# Extract the table header
table_header = parser.parse_train_delay_table_header(table)

# Getting the Table Body
table_body = parser.parse_train_delay_table_body(table)

# Extracting the other stuff
dates = parser.parse_train_delay_table_dates(table_body)
times = parser.parse_train_delay_table_times(table_body)
messages = parser.parse_train_delay_table_msg(table_body)

for entry in range(0, len(dates)):
    print('Datum: {} | Uhrzeit: {} | MSG: {}'.format(
        dates[entry], dates[entry], messages[entry]))
