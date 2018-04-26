#!/bin/sh

#  scraper.sh
#  
#
#  Created by Frances Sin on 2018-04-25.
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import ssl
import datetime

init ();

theatres = [ "scotiabank-theatre-vancouver",
             "fifth-avenue-cinemas",
             "the-park-theatre",
             "cineplex-cinemas-marine-gateway-and-vip",
             "cineplex-odeon-international-village-cinemas",
             "silverCity-riverport-cinemas" ]
            
print (Fore.BLUE + "\nCineplex Theatres in Vancouver:")

for index, theatre in enumerate(theatres, start = 1):
    print (Fore.RED + "[" + str (index) + "] " + theatre)
print (Fore.BLUE);

# Prompt user for theatre selection
user_selection = input ("Select a theatre: " + Fore.RED)

# Construct URL
now = datetime.datetime.now()
date = str (now.month) + '/' + str (now.day) + '/' + str (now.year)
theatre = theatres[int (user_selection) - 1]
url = 'https://www.cineplex.com/Showtimes/any-movie/' + theatre + '?Date=' + date


# Open connection and download webpage
context = ssl._create_unverified_context()
client = urlopen (url, context=context)
raw = client.read()
client.close()


# Parse HTML
soup = BeautifulSoup (raw, "html.parser")

cards = soup.findAll ("div", { "class":"h3 showtime-card--title" })

print (Fore.BLUE + "\n" + theatre.upper() + " is currently playing:")

for card in cards:
    title = card.meta["content"]
    print (Fore.YELLOW + str (title))

print ("")


