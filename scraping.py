import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

output = open('MO_election_results.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

br.select_form(nr = 0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003143']
br.form['ctl00$MainContent$cboRaces'] = ['460006719']

br.submit('ctl00$MainContent$btnCountyChange')

html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table',
    {'id': 'MainContent_dgrdCountyRaceResults'})

for row in main_table.find_all('tr'):
   data_1 = [cell.text.encode('utf-8') for cell in row.find_all('th')]
   writer.writerow(data_1)
   break
for row in main_table.find_all('tr'):
    data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
    writer.writerow(data)