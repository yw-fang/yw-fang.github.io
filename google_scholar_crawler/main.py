from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

# Extract citations and h-index
citations = author['citedby']
h-index = author['hindex']

# Save data as JSON
data = {
    "name": name,
    "updated": author['updated'],
    "citations": citations,
    "h-index": h-index
}

os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

# Create ShieldIO badge data for citations
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(citations),
}

with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# Create ShieldIO badge data for h-index
shieldio_data_h = {
    "schemaVersion": 1,
    "label": "h-index",
    "message": str(h-index),
}

with open(f'results/gs_data_h_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data_h, outfile, ensure_ascii=False)

