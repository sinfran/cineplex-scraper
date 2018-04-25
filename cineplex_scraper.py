#!/bin/sh

#  scraper.sh
#  
#
#  Created by Frances Sin on 2018-04-25.
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
from colorama import init, Fore
import ssl
import datetime

init (autoreset=True);

now = datetime.datetime.now()
date = str (now.month) + '/' + str (now.day) + '/' + str (now.year)

url = 'https://www.cineplex.com/Showtimes/any-movie/cineplex-cinemas-marine-gateway-and-vip?Date=' + date

# Open connection and download webpage
context = ssl._create_unverified_context()
client = urlopen (url, context=context)
raw = client.read()

client.close()

# Parse HTML
soup = BeautifulSoup (raw, "html.parser")

cards = soup.findAll ("div", { "class":"h3 showtime-card--title" })

print (Fore.RED + "Marine Drive is currently playing:")
for card in cards:
    title = card.meta["content"]
    print (str (title))

