import re
from locators.book_locators import Booklocators
class BOOK_PARSER:
    RATING={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def __init__(self,page):
        self.page=page
    def __repr__(self):
        return f'<Book{self.name},{self.price},{self.rating}stars>'

    @property
    def name(self):
        locator = Booklocators.NAME
        find_item = self.page.select_one(locator)
        item_name = find_item.attrs['title']
        return (item_name)

    @property
    def link(self):
        locator = Booklocators.LINK
        find_item = self.page.select_one(locator).attrs['href']
        return (find_item)

    @property
    def price(self):
        locator = Booklocators.PRICE_LOCATOR
        find_price = self.page.select_one(locator).string
        exp = '\$([0-9]+\.[0-9]+)'
        match = re.search(exp,find_price)
        return  find_price

    @property
    def rating(self):
        locator = Booklocators.RAITING
        find_rating = self.page.select_one(locator)
        clasess = find_rating.attrs['class']
        rating_calss = [find for find in clasess if find != 'star-rating']
        #print(rating_calss[0])
        rating_int=BOOK_PARSER.RATING.get(rating_calss[0])
        return rating_int



