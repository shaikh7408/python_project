import re
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parsers.page_parsers import BOOK_PARSER
class All_Books:
    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')
    def books(self):
        return [BOOK_PARSER(e)for e in self.soup.select(AllBooksPageLocators.BOOKS)]
    @property
    def page_count(self):
        content=self.soup.select_one(AllBooksPageLocators.PAGE_LOCATOR).string
        pattern='Page [0-9]+ of ([0-9]+)'
        match=re.search(pattern, content)
        pages=int(match.group(1))
        return pages

