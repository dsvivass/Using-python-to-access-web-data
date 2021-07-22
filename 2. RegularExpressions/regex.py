import requests
import re

url = 'http://py4e-data.dr-chuck.net/regex_sum_1308005.txt'
r = requests.get(url, allow_redirects=False)

text = r.content.decode('utf-8')

print(sum([int(i) for i in re.findall('[0-9]+', text)]))
