import sys

from requests_html import HTMLSession

def url_check(url, logger = None):

    session = HTMLSession()

    r = session.get(url)

    if r.ok:
        return(r)
    else:
        if not logger == None:
            logger.critical(f'URL response code bad: {r.status_code}')
        else:
            sys.exit(f'URL response code bad: {r.status_code}')
