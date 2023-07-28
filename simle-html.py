from bs4 import BeautifulSoup
simple_html='''<html>
<head></head>
<body>
<h1>This is title</h1>
<p class="subtitle"> indendent class paragram</p>
<p>here is another without class para</p>
<ul>
<li>imad</li>
<li>motin</li>
<li>shaikh</li>
<li>fiazan</li>
</ul>
</body>
</html>
'''
simple_soup=BeautifulSoup(simple_html,'html.parser')

def find_allparagaph():
    paragraph=simple_soup.find_all('p')
    other_para=[p for p in paragraph if 'subtitle' not in p.attrs.get('class',[])]
    print(other_para[0].string)
find_allparagaph()


