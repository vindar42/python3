#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.exchangerates.org.uk/Dollars-to-Egyptian-Pounds-currency-conversion-page.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.findChildren("div", {"class": "p_conv30"})[1].get_text().split()

integer = float(tags[3])
user = input("Please Enter USD: ")

def exchange_USD(user , integer):
	return float(user) * integer

print (user,"USD cost in EGP",exchange_USD(user, integer))
