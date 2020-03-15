from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client request
import urllib.request, urllib.error # .request error handling library (Try, Except)
import datetime
import os
import codecs

page_url = ('https://boards.lt/en/home/10680-22836-nitro-2020-squash-snowboard.html')
print(page_url)
try: #2.Scraping (attempt to read)
    conn = urllib.request.urlopen(page_url) #opened connection to page_url
except urllib.error.HTTPError as e: #skip 404 pages
    pass
    # Return code error (e.g. 404, 501, ...)
    #print('HTTPError: {}'.format(e.code))
except urllib.error.URLError as e: #skip unrequestable pages
    pass
    # Not an HTTP-specific error (e.g. connection refused)
    # print('URLError: {}'.format(e.reason))
else:
    # 200
    page_soup = soup(conn.read(), "html.parser", from_encoding="utf-8")
    conn.close() #closing open connection as page is read to memory
    print(page_soup)