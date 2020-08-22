import requests, sys, bs4, webbrowser
keywords = sys.argv[1]
url = "https://www.baidu.com/s?ie=utf-8&csq=1&pstg=20&mod=2&isbd=1&cqid=ad36a6c300004cc7&istc=1254&ver=RAtwGdIJ_3Taje7bpfWDye9W0LVqWyiQEYS&chk=5f3f1c8c&isid=FF082E0D06228973&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=test&fenlei=256&rsv_pq=f1e8b47500006913&rsv_t=3790MzvNyhFmBHqJiuqrAUAJqaF%2FdpUodvrCM1UtDjtyYr4nBhRjJLLSf9w&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=6&rsv_sug1=7&rsv_sug7=101&rsv_btype=i&prefixsug=" + keywords + "&rsp=9&inputT=53007&rsv_sug4=53007&f4s=1&_ck=1356.1.168.36.26.736.41&rsv_isid=1468_32568_32538_32046_32117_31321_26350_32507&isnop=1&rsv_stat=-2&rsv_bp=1"
print(url)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
res = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(res.text, "lxml")
link_elems = soup.select('.c-showurl ')

num_open = min(5, len(link_elems))
for i in range(num_open):
    print(link_elems[i+1].get('href'))
    # webbrowser.open(link_elems[i+1].get('href'))






