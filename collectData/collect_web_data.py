import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Python'
request = requests.get(url)
extraction = BeautifulSoup(request.text, 'html.parser')

#Display Text
#print(extraction.text.strip())

#Filter display by tag (h2)
for text_line in extraction.find_all('h2'):
    title = text_line.text.strip()
print(f'Title: {title}')

#Filter display by tag (p)
for text_line in extraction.find_all('p'):
    paragraph = text_line.text.strip()
    print(f'Paragraph: {paragraph}')

#Count tags
count_h2 = 0
count_p = 0
for text_line in extraction.find_all(['h2', 'p']):
    if text_line.name == 'h2':
        count_h2 += 1
    elif text_line.name == 'p':
        count_p += 1
print(f'\nTitle: {count_h2}')
print(f'Paragraph: {count_p}')

#Display nested tags
for title in extraction.find_all('h2'):
    print(f'\nTitle: {title.text.strip()}')
    for link in title.find_next_siblings(['p', 'ul', 'ol']):
        for a in link.find_all('a', href=True):
                print(f'Text Link: {a.text.strip()} | URL:{a['href']}')

