import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        print('Downloading page http://xkcd.com/%s...' % (url_number))
        res = requests.get('http://xkcd.com/%s' % (url_number))
        # print(res.status_code)
        res.raise_for_status
        soup = bs4.BeautifulSoup(res.text, "lxml")
        comic_elem = soup.select('#comic img')
        print(comic_elem)
        if comic_elem == []:
            print("Could not find cominc image.")
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.status_code

            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

download_threads = []

# download_xkcd(2, 3)
for i in range(2, 1403, 100):
    print(i)
    download_thread = threading.Thread(target=download_xkcd, args=(i, i+99))
    download_threads.append(download_thread)
    download_thread.start()


        


