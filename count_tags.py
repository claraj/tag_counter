import requests 
from bs4 import BeautifulSoup
from pie import draw_pie

# For downloading...
url = 'https://www.minneapolis.edu' # todo fill in here
page = requests.get(url).text

# for reading from a file...
# page = open('page.html', 'r').read()


soup = BeautifulSoup(page, 'html.parser')

all_tags = soup.find_all(True)

names = [ tag.name for tag in all_tags ]

tag_counts = {}

for name in names:
    if name in tag_counts:
        tag_counts[name] = tag_counts[name] + 1
    else:
        tag_counts[name] = 1

# print(tag_counts)

draw_pie(tag_counts, "pie_plot.html")

# Tags covered in class in the first week

week_1_tags = ['p', 'a', 'b', 'img', 'div', 'span', 'i', 
'table', 'td', 'tr', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
'link', 'html', 'body', 'title', 'head', 'li', 'ul', 'ol', 'br', 'strong']

week_2_tags = ['option', 'select', 'button', 'input', 'form']

known_vs_unknown = {
    'known': 0,
    'unknown': 0
}

unknown_set = set()

for name in names:
    if name in week_1_tags:
        known_vs_unknown['known'] += 1
    else:
        unknown_set.add(name)
        known_vs_unknown['unknown'] += 1

print(f'unknown tags: {unknown_set}')
print(known_vs_unknown)

if known_vs_unknown['known'] + known_vs_unknown['unknown'] == 0:
    # no tags!
    print('There are no tags.')
else:
    percentage_known = known_vs_unknown['known'] / ( known_vs_unknown['known'] + known_vs_unknown['unknown'] )  * 100
    draw_pie(known_vs_unknown)
    print(f'This page has {percentage_known:.1f}% known tags.')
