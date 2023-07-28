import re

import soupsieve
from  bs4 import BeautifulSoup
ITEM_HTML= '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">$51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''
class Itmem_locator:
    Name_locator='article.product_pod h3 a'
    Link_locator = 'article.product_pod h3 a'
    Price_locator = 'article.product_pod p.price_color'
    Rating_locator = 'article.product_pod p.star-rating'
class ancaps:
    def __init__ (self,page):
        self.middle_soup=BeautifulSoup(page,'html.parser')
    @property
    def name(self):
        locator = Itmem_locator.Name_locator
        find_item = self.middle_soup.select_one(locator)
        item_name = find_item.attrs['title']
        return (item_name)
    @property
    def link(self):
        locator = Itmem_locator.Link_locator
        find_item =self.middle_soup.select_one(locator).attrs['href']
        return (find_item)
    @property
    def price(self):
        locator = Itmem_locator.Price_locator

        find_price =self.middle_soup.select_one(locator).string
        exp = '\$([0-9]+\.[0-9]+)'
        match = re.search(exp,find_price)
        return (float(match.group(1)))
    @property
    def rating(self):
        locator = Itmem_locator.Rating_locator
        find_rating=self.middle_soup.select_one(locator)
        clasess = find_rating.attrs['class']
        rating_calss = [find for find in clasess if find != 'star-rating']
        return rating_calss[0]


object=ancaps(ITEM_HTML)
print(object.rating)
print(object.price)
print(object.link)
print(object.name)

