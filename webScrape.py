import requests
import sys

EMAIL = 'fill these in'
PASSWORD = ''

URL = 'https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtHome'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session()

    # This is the form data that the page sends when logging in
    login_data = {
        'username': EMAIL,
        'password': PASSWORD,
        'mySubmit': 'Log In',
    }

    # Authenticate
    r = session.post(URL, data=login_data)
    print r

    # Try accessing a page that requires you to be logged in
    r = session.get('https://oasis-sso.publix.org/ESS/rp/0458/ESS#Taskflow.ESS:mtSchedule')
    print r
    print r.text

if __name__ == '__main__':
    main()
