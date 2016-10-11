import urllib
import re
from twill.commands import *

# Gather input from the user
username = raw_input('Enter username: ')
password = raw_input('Enter password: ')
url = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'

# Go to the specified URL
go(url)

# FormValue (fv) finds the specified form, then the specified field in that form
# and populates that field with the third argument
fv("myForm", "username", username)
fv("myForm", "password", password)

# Submit our filled out form. Searches the form for a submit field and uses it
submit('0')

# Get the text from the page, now that we are logged in
htmlfile = urllib.urlopen("https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome")
htmltext = htmlfile.read()

# If we are logged in, this should print "Oasis", if not it will print "Login"
regex = '<title>(.*)</title>'
pattern = re.compile(regex)
print re.findall(pattern,htmltext)

# This will retrieve the string for when our next shift is
# of the format Thursday 11:30am - 8:30pm
regex = '<div class="x-grid3-cell-inner x-grid3-col-Shift" unselectable="on">(.+?)</div>'

pattern = re.compile(regex)

shift = re.findall(pattern,htmltext)
print shift
