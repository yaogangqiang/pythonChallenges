import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url_fragment = '12345'

def extract_number(string):
    p = re.compile(r'\d+')
    number = ''.join(p.findall(string))
    if number == '16044':
        number = '8022'
    if number == '8268363579':
        number = '63579'
    return number

for i in xrange(400):
     URL = url + url_fragment
     string = urllib.urlopen(URL).read()
     print string 
     url_fragment = extract_number(string)  
    

