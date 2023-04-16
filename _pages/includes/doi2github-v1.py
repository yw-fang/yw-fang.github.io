import re

# Open the input file
with open('1.txt', 'r') as f:
    content = f.read()

# Get the author list
author_match = re.search(r'author = {(.+)}', content)
authors = author_match.group(1).split(' and ')

# Check if Yue-Wen Fang is in the author list
yuewen_fang = False
for i, author in enumerate(authors):
    if 'Yue-Wen Fang' in author:
        yuewen_fang = True
        authors[i] = '<b>Yue-Wen Fang</b>'
    elif 'Fang, Yue-Wen' in author:
        yuewen_fang = True
        last_name, first_name = author.split(', ')
        authors[i] = f'<b>{first_name} {last_name}</b>'
    else:
        last_name, first_name = author.split()
        authors[i] = f'{first_name} {last_name}'

# Get the remaining fields
title_match = re.search(r'title = {(.+)}', content)
journal_match = re.search(r'journal = {(.+)}', content)
year_match = re.search(r'year = {(.+)}', content)
volume_match = re.search(r'volume = {(.+)}', content)
issue_match = re.search(r'issue = {(.+)}', content)
pages_match = re.search(r'pages = {(.+)}', content)
doi_match = re.search(r'doi = {(.+)}', content)
url_match = re.search(r'url = {(.+)}', content)

# Generate the HTML
html = '<tr>\n  <td style="vertical-align: top; padding-right: 20px;">\n    <p>40. {}, <a href="{}"><i>{}</i></a>, {}, {}, '.format("; ".join(authors), url_match.group(1), title_match.group(1), journal_match.group(1), year_match.group(1))

if volume_match:
    html += '{}'.format(volume_match.group(1))
    if issue_match:
        html += '({}): '.format(issue_match.group(1))
    else:
        html += ': '
else:
    html += ' : '
    
if pages_match:
    html += '{}.'.format(pages_match.group(1))
else:
    html += '.'

html += '</p>\n  </td>\n  <td style="vertical-align: top;">\n    <a href="{}"><img src="./journal-cover/cover.png" alt="cover" width="500"></a>\n  </td>\n</tr>'.format(url_match.group(1))

# Print the HTML
print(html)

