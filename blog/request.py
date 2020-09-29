import urllib.request, json
from .models import Quotes


base_url = None

def configure_request(app):
  global base_url
  base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes():
  count=0
  quotes=[]
  while count!=4:
    with urllib.request.urlopen(base_url) as url:
      get_quotes_data = url.read()
      get_quotes_response = json.loads(get_quotes_data)
    if get_quotes_response:
      quote_text=get_quotes_response['quote']
      quote_author=get_quotes_response['author']

      quote_object = Quotes(quote_text,quote_author)
      quotes.append(quote_object)
    count=count+1

  return quotes

