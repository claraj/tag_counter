import requests 
from bs4 import BeautifulSoup
from pie import draw_pie
import sys

# For downloading...
url = 'https://www.minneapolis.edu' # todo fill in here
page = requests.get(url).text

# Or, for reading from a file...
page = open('page.html', 'r').read()

soup = BeautifulSoup(page, 'html.parser')

all_tags = soup.find_all(True)

names = [ tag.name for tag in all_tags ]   # List comprehension

if not names:
    print('There are no tags in this data.')
    sys.exit()

tag_counts = { name: names.count(name) for name in names }  # dictionary comprehension!

# Pie chart with frequencies for all the tags in the document 
draw_pie(tag_counts, 'pie_plot.html')

# How many of these tags are ones we know? 
# Tags covered in class in the first week

week_1_tags = ['p', 'a', 'b', 'img', 'div', 'span', 'i', 
'table', 'td', 'tr', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
'link', 'html', 'body', 'title', 'head', 'li', 'ul', 'ol', 'br', 'strong']

# TODO - what about the following week? 
week_2_tags = ['option', 'select', 'button', 'input', 'form', 'pre', 'code']

known_tags = week_1_tags + week_2_tags

known_vs_unknown = {
    'known': 0,
    'unknown': 0
}

# Set comprehensions 
unknown_set = { name for name in names if name not in known_tags }

for name in names:
    if name in known_tags:
        known_vs_unknown['known'] += 1
    else:
        known_vs_unknown['unknown'] += 1

print(f'unknown tags: {unknown_set}')
print(known_vs_unknown)

if known_vs_unknown['known'] + known_vs_unknown['unknown'] == 0:
    # avoid possible divide by zero error 
    print('There are no tags.')
else:
    percentage_known = known_vs_unknown['known'] / ( known_vs_unknown['known'] + known_vs_unknown['unknown'] )  * 100
    draw_pie(known_vs_unknown)
    print(f'This page has {percentage_known:.1f}% known tags.')
