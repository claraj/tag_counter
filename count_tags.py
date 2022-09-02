import requests 
from bs4 import BeautifulSoup
from pie import draw_pie
import sys


url = 'https://www.minneapolis.edu' # todo fill in here
# For downloading...

try:
    page = requests.get(url).text
except:
    print(f'error downloading site {url}')
    exit()

# Or, for reading from a file...
# page = open('page.html', 'r').read()

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

week_1_tags = {'p', 'a', 'b', 'img', 'div', 'span', 'i', 
'table', 'td', 'tr', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
'link', 'html', 'body', 'title', 'head', 'li', 'ul', 'ol', 'br', 'strong'}

# TODO - what about the following week? 
week_2_tags = {'option', 'select', 'button', 'input', 'form', 'pre', 'code'}

# known_tags = week_1_tags.union(week_2_tags)   # argument to union can be any iterable
known_tags = week_1_tags | week_2_tags  # union operator, join two sets
# note that & returns the intersection, the common items in both sets
# The - operator returns the difference - remove items in second set from the first set

known_vs_unknown = {
    'known': 0,
    'unknown': 0
}

# Set comprehensions 
unknown_set = { name for name in names if name not in known_tags }

# Or, in a more set-like way,
all_tags_set = set(names)
unknown_set = all_tags_set - known_tags  # difference operator

for name in names:
    if name in known_tags:
        known_vs_unknown['known'] += 1
    else:
        known_vs_unknown['unknown'] += 1

print(f'unknown tags: {unknown_set}')
print(known_vs_unknown)

known_count = known_vs_unknown['known']
unknown_count = known_vs_unknown['unknown']
total_count = known_count + unknown_count

if total_count == 0:
    # avoid possible divide by zero error 
    print('There are no tags.')
else:
    percentage_known = known_count / total_count  * 100
    draw_pie(known_vs_unknown)
    print(f'This page has {percentage_known:.1f}% known tags.')
