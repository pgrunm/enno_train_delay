from enno_train_delay import enno_train_delay


def main():

    url = 'https://der-enno.de/#meldungen'
    parser = enno_train_delay.extract_train_delay_information()
    table_content = parser.parse_train_delay_table(url)

    # This should only be true if there are no delays.
    if len(table_content) == 2:
        print('Keine Meldungen vorhanden!')
    else:
        for line in table_content:
            # Contains header
            if 'Datum' in line and 'Uhrzeit' in line and 'Meldung' in line:
                # Nothing yet...
                pass

            # Line contains the beautiful data we want
            else:
                date = parser.parse_train_delay_table_date(line)
                time = parser.parse_train_delay_table_time(line)
                msg = parser.parse_train_delay_table_msg(line)

                print('{} um {}: {}'.format(date, time, msg))


if __name__ == '__main__':
    main()
