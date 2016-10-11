import urllib
import urllib2
import cookielib
import re

# Login function, not exactly sure how this works yet
def login(url, data):
    response = opener.open(url, data)
    the_page = response.read()
    http_headers = response.info()
    return ''.join(response.readlines())

username = raw_input('Enter username: ')
password = raw_input('Enter password: ')
url = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'
values = {'username' : username,
          'password' : password}

# Encode our data and gather our cookies
data = urllib.urlencode(values)
cookies = cookielib.CookieJar()

# Open a session, unsure what exactly this does
opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cookies))

# Call login twice, once to establish cookies, once to login
login(url, data)
login(url, data)

# Gather html data
htmlfile = urllib.urlopen("https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome")
htmltext = htmlfile.read()

# We are interested in the date and time string that the regex will pull
# it will be in the format Thursday 11:30am - 8:00pm
regex = '<div class="x-grid3-cell-inner x-grid3-col-Shift" unselectable="on">(.+?)</div>'
pattern = re.compile(regex)

# Find and store the time when our shift starts and ends, and print it
shift = re.findall(pattern,htmltext)
print shift
