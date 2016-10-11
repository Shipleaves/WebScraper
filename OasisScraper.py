import urllib
import re
from twill.commands import *

url = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'

go(url)

fv("myForm", "username", "")
fv("myForm", "password", "")

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
