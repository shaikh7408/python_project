
from bs4 import BeautifulSoup
from locators.quote_page_locator import QuotesPageLocatrs
from parsers.quotes import QuoteParser
class QuotesPage:
    def __init__(self,page):
       self.soup=BeautifulSoup(page,'html.parser')
      # print(self.soup)
    @property
    def quotes(self):
        locator=QuotesPageLocatrs.QUOTE
        #print(locator)
        quote_tags=self.soup.select(locator)
       #print(quote_tags)
        return [QuoteParser(e)for e in quote_tags]


