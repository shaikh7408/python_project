
from locators.quote_locator import QuoteLocators

class QuoteParser:
    def __init__(self,parents):
        self.parents=parents
    def __repr__(self):
        return f'QUOTE{self.content}.BY{self.author}'
    @property
    def content(self):
        locators=QuoteLocators.CONTENT
        return self.parents.select_one(locators).string
    @property
    def author(self):
        locators=QuoteLocators.AUTHOR
        return self.parents.select_one(locators).string
    @property
    def tags(self):
        locators=QuoteLocators.TAGS
        #print(locators)
        return [e.string for e in self.parents.select(locators)]

