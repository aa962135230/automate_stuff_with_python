import bs4, requests

url = 'http://www.caitec.org.cn/'

res = requests.get(url)
res.status_code

bs_obj = bs4.BeautifulSoup(res.text, "lxml")
href_links = bs_obj.select('a[href]')

for i in range(len(href_links)):
    pending_link = href_links[i].get('href')

    if pending_link.startswith('http:'):
        processed_link = pending_link
    else:
        processed_link = url + pending_link

    sub_res = requests.get(processed_link)
    if sub_res.status_code == 404:
        print("%s 404 Not Found" % (processed_link))
    else:
        print("%s Found" % (processed_link))
    



