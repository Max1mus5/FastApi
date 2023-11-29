from datetime import datetime
from typing import Any

import requests
from bs4 import BeautifulSoup as Soup
from pytz import timezone, UTC

URL = 'https://www.rottentomatoes.com'
TIMEZONE = 'America/Mexico_City'

def pages(page: str) -> dict[Any]:
   request = requests.get(f'{URL}/{page}')
   html = Soup(request.content, 'html.parser')
   
   #search slot
   buttons = html.find_all(attrs={'slot': True})
   
   data = []
   for button in buttons:
      # Search especific button
      if (button['slot'] == page or page == 'browse') and button['slot'] in ['movies', 'tv', 'showtimes','news', 'trivia']:
          row = {'slot': button['slot'], 'name': button.text.replace('\n', '-') or button.text.remplace('\t',''), 'link': button.find('a')['href']}
          data.append(row)

   return {'total': len(data), 'page': page, 'items': data}



def screen(page:int) -> dict[Any]: 
   request = requests.get(f'{URL}/browse/movies_in_theaters/?page={page}')
   print(f'{URL}/browse/movies_in_theaters/?page={page}')
   html = Soup(request.content, 'html.parser')
   #search in div class="discovery-tiles" all the elements with <a class="js-tile-link "> 
   card = html.find_all(attrs={'data-id':'movies_in_theaters'})[0].find_all(attrs={'data-qa':"discovery-media-list-item"})
   print(card[0])
   movieData = []
   for index, movieCard in enumerate(card):
        title = movieCard.find('span', {'data-qa': 'discovery-media-list-item-title'}).text.strip()
        score_element = movieCard.find('score-pairs-deprecated', {'criticsscore': True})
        if score_element:
            score = score_element['criticsscore']
        else:
            score = "Score not available"
        rank_element = movieCard.find('score-pairs-deprecated', {'criticssentiment': True})
        if rank_element:
            rank = rank_element['criticssentiment']
        else:
            rank = "Score not available"
        date = movieCard.find('span', {'data-qa': 'discovery-media-list-item-start-date'}).text.strip()
        link = f'{URL}/m/{title.replace(" ", "_").replace(":", "").lower()}'
        movieROW = {
            'index': index + 1,
            'title': title,
            'score': score,
            'rank': rank,
            'date': date,
            'link': link
        }
        movieData.append(movieROW)

   return {'total': len(movieData), 'page': page, 'items': movieData} 

