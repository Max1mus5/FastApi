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
      # Comprobar si el botón tiene los valores que estás buscando
      if (button['slot'] == page or page == 'browse') and button['slot'] in ['movies', 'tv', 'showtimes','news', 'trivia']:
          row = {'slot': button['slot'], 'name': button.text, 'link': button.find('a')['href']}
          data.append(row)

   return {'total': len(data), 'page': page, 'items': data}
