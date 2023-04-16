import re

import unicodedata

def to_ascii(in_string):
    # Replace Unicode dashes with ASCII hyphen-minus
    out_string = in_string.replace('\u2013', '-').replace('\u2014', '-')
    return(out_string)

# my_string = "example-string—containing–dashes"
# print(my_string)
# print(to_ascii(in_string=my_string))



# Open the input file
with open('1.txt', 'r') as f:
    content = f.read()

# Get the author list
author_match = re.search(r'author = {(.+)}', content)
authors_string = author_match.group(1)
# print(authors_string)
# Remvoe spaces at the beginning of the string
def remove_spaces(in_string):
    out_string = in_string
    while out_string.startswith(" "):
        out_string = out_string[1:]
    # Check for spaces at the end of the string
    while out_string.endswith(" "):
        out_string = out_string[:-1]
    return out_string
#    print(authors_string)
#print(authors_string)
authors_string = remove_spaces(authors_string)
to_ascii(authors_string)
#print(authors_string)
authors = authors_string.split(' and ')
# print(authors)


# Check if Yue-Wen Fang is in the author list
yuewen_fang = False
for i, author in enumerate(authors):
    if ('Yue'+'-'+'Wen') in author:
        yuewen_fang = True
        last_name, first_name = author.split(', ')
        authors[i] = f'<b>{first_name} {last_name}</b>'
    else:
        last_name, first_name = author.split(',')
#        print(last_name, first_name)
        authors[i] = f'{first_name} {last_name}'
#print(yuewen_fang)
#print(authors)

# Get the remaining fields
title_match = re.search(r'title = {(.+)}', content)
journal_match = re.search(r'journal = {(.+)}', content)
journal_match_string = journal_match.group(1)
# print('journal_match is', journal_match.group(1), 'type is', type(journal_match.group(1)), 'length is', len(journal_match_string))
journal_match_string = remove_spaces(journal_match_string)
# print('journal_match is', journal_match.group(1), 'type is', type(journal_match.group(1)), 'length is', len(journal_match_string))
#  21 author_match = re.search(r'author = {(.+)}', content)
#  22 authors_string = author_match.group(1)

year_match = re.search(r'year = {(.+)}', content)
year_match_string = remove_spaces(year_match.group(1))
volume_match = re.search(r'volume = {(.+)}', content)
issue_match = re.search(r'issue = {(.+)}', content)
pages_match = re.search(r'pages = {(.+)}', content)
doi_match = re.search(r'doi = {(.+)}', content)
url_match = re.search(r'url = {(.+)}', content)


# Generate the HTML
# html = '<tr>\n  <td style="vertical-align: top; padding-right: 20px;">\n    <p>40. {}, <a href="{}"><b>{}</b></a>, {}, {}, '.format("; ".join(authors), url_match.group(1), title_match.group(1), journal_match.group(1), year_match.group(1))
html = '<tr>\n  <td style="vertical-align: top; padding-right: 20px;">\n    <p>40. {}, <a href="{}"><b>{}</b></a>, {}, {}, '.format("; ".join(authors), url_match.group(1), title_match.group(1), journal_match_string, year_match_string)

if volume_match:
    html += '{}'.format(remove_spaces(volume_match.group(1)))
    if issue_match:
        html += '({}): '.format(remove(issue_match.group(1)))
    else:
        html += ': '
else:
    html += ' : '
    
if pages_match:
    html += '{}.'.format(remove_spaces(pages_match.group(1)))
else:
    html += '.'

html += '</p>\n  </td>\n  <td style="vertical-align: top;">\n    <a href="{}"><img src="./journal-cover/cover.png" alt="cover" width="500"></a>\n  </td>\n</tr>'.format(url_match.group(1))

# Print the HTML
print('\n')
print('copy the following html to the markdown file')
print(html)

