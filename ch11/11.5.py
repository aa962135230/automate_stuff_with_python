import requests, bs4

print('****11.5.1****')
# res = requests.get('http://nostarch.com')
# print(res.raise_for_status())
# example_file = open('example.html', 'w')
# example_file.write(res.text)
# example_file.close()

# no_starch_soup = bs4.BeautifulSoup(res.text)
# print(type(no_starch_soup))

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file.read(), "lxml")
print("example_soup type: " + str(type(example_soup)))


print('****11.5.2****')
elems = example_soup.select('#node-560')
print("elems type is: " + str(type(elems)))
print(len(elems))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

p_elems = example_soup.select('p')
print(len(p_elems))
print(str(p_elems[0]))
print(p_elems[0].getText())

print(str(p_elems[1]))
print(p_elems[1].getText())

print(str(p_elems[2]))
print(p_elems[2].getText())


print('****11.5.3****')

soup = bs4.BeautifulSoup(open('example.html'), "lxml")
span_elem = soup.select('span')[0]
print(str(span_elem))

print(span_elem.get('id'))