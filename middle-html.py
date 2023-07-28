import re

import soupsieve
from  bs4 import BeautifulSoup
ITEM_HTML = '''<html><head></head><body>
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
middle_soup=BeautifulSoup(ITEM_HTML,'html.parser')
def find_attribute():
    locator='article.product_pod h3 a'
    #print(middle_soup)
    find_item = middle_soup.select_one(locator)
   # print(find_item)
    item_name=find_item.attrs['title']
    print(item_name)
find_attribute()
def find_attribute_href():
    locator='article.product_pod h3 a'
   # print(middle_soup)
    find_item = middle_soup.select_one(locator).attrs['href']
    print(find_item)
    #item_name=find_item.attrs['href']
    #print(item_name)
find_attribute_href()
def find_attribute_price():
    locator='article.product_pod p.price_color'

    find_price = middle_soup.select_one(locator).string
    exp= '\$([0-9]+\.[0-9]+)'
    print(find_price)
    match=re.search(exp,find_price)
    print(match)
    print(match.group(0))
    print(float(match.group(1)))
    #print(find_item.string)
    #item_name=find_item.attrs['href']
    #print(item_name)
find_attribute_price()
def find_attribute_rating():
    locator='article.product_pod p.star-rating'
   # print(middle_soup)
    find_rating = middle_soup.select_one(locator)
    #print(find_rating)
    clasess=find_rating.attrs['class']
    print(clasess)
    rating_calss=[find for find in clasess if find!='star-rating']
    print(rating_calss[0])


    #item_name=find_item.attrs['href']
    #print(item_name)
find_attribute_rating()


