import HTMLTableParser as h
import requests


url = 'https://www.der-enno.de/#meldungen'
# response = requests.get(url)
# response.text[:100]  # Access the HTML with the text property
hp = h.HTMLTableParser()
# table = hp.parse_url(url)  # [0][1]  # Grabbing the table from the tuple
table = hp.test()
print(table)
