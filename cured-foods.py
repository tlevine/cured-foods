import requests
import lxml.html

url = 'https://en.wikipedia.org/wiki/List_of_pickled_foods'
r = requests.get(url, headers = {'User-Agent': 'Mozilla'})
html = lxml.html.fromstring(r.content)
html.make_links_absolute(url)
texts = html.xpath('id("mw-content-text")/descendant::a/text()')
foods = list(filter(lambda x: 'List' not in x and 'wiki' not in x.lower(), texts))

result = ''
while result.count(' ') < 99:
    result += random.choice(foods) + ' '
result = result.strip()
print(result)
