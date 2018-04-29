#!/bin/sh

#  scraper.sh
#  
#
#  Created by Frances Sin on 2018-04-25.
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import ssl
import datetime

init ();

theatres = [ "scotiabank-theatre-vancouver",
             "fifth-avenue-cinemas",
             "the-park-theatre",
             "cineplex-cinemas-marine-gateway-and-vip",
             "cineplex-odeon-international-village-cinemas",
             "silverCity-riverport-cinemas" ]

print (Style.BRIGHT + "\n")
print (Fore.BLUE + "Cineplex Theatres in Vancouver:")

for index, theatre in enumerate(theatres, start = 1):
    print (Fore.RED + "[" + str (index) + "] " + theatre)
print (Fore.BLUE);

# Prompt user for theatre selection
user_input = input ("Select theatres(s): " + Fore.GREEN)
user_selections = list (map (int, user_input.replace (" ", "").split(',')))

# Construct URL
now = datetime.datetime.now()
date = str (now.month) + '/' + str (now.day) + '/' + str (now.year)


for i in user_selections:
    theatre = theatres[i - 1]
    url = 'https://www.cineplex.com/Showtimes/any-movie/' + theatre + '?Date=' + date

    # Open connection and download webpage
    context = ssl._create_unverified_context()
    client = urlopen (url, context=context)
    raw = client.read()
    client.close()

    # Parse HTML
    soup = BeautifulSoup (raw, "html.parser")

    movies = soup.findAll ("div", { "class":"h3 showtime-card--title" })
    showtimes = soup.findAll ("div", { "class": "showtime-card showtime-single" })
    
    print (Fore.RED + "\n<" + theatre.upper() + "> is currently playing:")

    for index, movie in enumerate (movies):
        title = movie.meta["content"]
        all_times = "";

        print (Fore.YELLOW + " > " + str (title))
        
        
        
        #print (showtimes[index].findAll ("div", { "class": "grid__item one-whole" }))
        
        # print (showtimes[index].findAll("div", { "class": "grid showtime--item" }))   , { "class": "showtime--list" })
        
        
        for index, times in enumerate (showtimes[index].findAll("li")):
            
            if index == 0:
                all_times = str (times.meta["content"])
            else:
                all_times = all_times + ", " + str (times.meta["content"])

        
        print (Style.NORMAL + "   [" + all_times + "]" + Style.BRIGHT)
# print (" " + Fore.WHITE + str (times.meta["content"]))
     
        


print (Style.RESET_ALL + "")


