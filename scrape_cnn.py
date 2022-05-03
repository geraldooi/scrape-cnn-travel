'''
CNN Travel Scraper

This python script is used to scrape CNN Travel article byline into a text files.

Authors:
  Gerald Ooi
  Website: geraldooi.com

URLs:
- https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html
- https://edition.cnn.com/travel/article/new-maldives-luxury-resorts-spc-intl/index.html
'''
import requests as req
import sys

from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema, InvalidURL

def scrape_cnn(url):
  '''Returns the article scrape line by line in a list by providing CNN Travel article's URL.

    Parameters:
      url (string): A string of url to a CNN Travel article
    
    Returns:
      contents_list (list): List of article byline
  '''
  try:
    # Get HTML from the url given
    # Parse it to BeautifulSoup
    res = req.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # Select the content from <body></body> only
    body = soup.select('body')[0]

    # Extract article branding, title, author and updated date
    # Append it to the content_list in sequence
    article_branding = body.select_one('.Article__branding').text.strip()
    article_title = body.select_one('.Article__title').text.strip()
    article_subtitle = body.select_one('.Article__subtitle').text.strip().split(' • ')
    article_author = article_subtitle[0].split(',')[0]
    article_updated_date = article_subtitle[1][8:]

    # Extract article paragraph
    paragraph_components = body.select('.Paragraph__component')
    test = [comp.text for comp in paragraph_components]
    
    return [
      article_branding, article_title, article_author, article_updated_date,
      *[comp.text.strip() for comp in paragraph_components]
    ]
  
  except (MissingSchema, InvalidURL):
    print(f'Invalid URL \'{url}\'. Please check you have input the right URL.')
    return None

if __name__ == '__main__':
  # Check for system args
  try:
    url = sys.argv[1]
  
  # If no system args provided, get user input instead
  except IndexError:
    print('We\'ve noticed run this script without provide url as argument.')
    url = input('Enter CNN URL: ')

  # Used part of URL as output filename
  output_filename = url.split('/')[5]

  # scrape cnn article from the url given
  results = scrape_cnn(url)

  # write result to txt file if results not null
  if results is not None:
    with open(f'{output_filename}.txt', 'w') as f:
      f.write('\n'.join(map(lambda x: str(x), results)))