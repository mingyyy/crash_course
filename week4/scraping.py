from requests_html import HTMLSession
# url="https://en.wikipedia.org/wiki/Ubud"
# url = "https://www.booking.com/searchresults.en-gb.html?city=-2701757"
url = "https://www.instagram.com/martin.breuss/"
session = HTMLSession()
r = session.get(url)
r.html.render() # parse JavaScript TODO look into parse JS


for link in r.html.absolute_links:
    print(link)

# # using css selectors
# history = r.html.find('#History', first=True) # DSS id=History (fragment = internal link)
#
# # XPATH
# content = r.html.xpath('//*[@id="mw-content-text"]/div', first = True)
# ps = content.find('p')
# for p in ps:
#     print(p.text, end='\n\n')
#
# # spider


