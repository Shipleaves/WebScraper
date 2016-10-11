import urllib
import re
from twill.commands import *

username = raw_input('Enter username: ')
password = raw_input('Enter password: ')
url = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'

go(url)

fv("myForm", "username", username)
fv("myForm", "password", password)

submit('0')

htmlfile = urllib.urlopen("https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome")
htmltext = htmlfile.read()

regex = '<title>(.*)</title>'
pattern = re.compile(regex)
print re.findall(pattern,htmltext)

regex = '<div class="x-grid3-cell-inner x-grid3-col-Shift" unselectable="on">(.+?)</div>'

pattern = re.compile(regex)

shift = re.findall(pattern,htmltext)
print shift
