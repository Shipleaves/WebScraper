import urllib
import urllib2
import cookielib
import re

def login(url, data):
    response = opener.open(url, data)
    the_page = response.read()
    http_headers = response.info()
    return ''.join(response.readlines())


url = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'
values = {'username' : '',
          'password' : ''}

data = urllib.urlencode(values)
cookies = cookielib.CookieJar()

opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cookies))

login(url, data)
login(url, data)

htmlfile = urllib.urlopen("https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome")
htmltext = htmlfile.read()

regex = '<div class="x-grid3-cell-inner x-grid3-col-Shift" unselectable="on">(.+?)</div>'
pattern = re.compile(regex)

shift = re.findall(pattern,htmltext)
print shift
