import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone
import os

# Google Scholar Profile URL
URL = "https://scholar.google.com/citations?user=6NU1KPQAAAAJ&hl=en"

# Set up request headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}

# Make the HTTP request
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print("DEBUG: Response status code:", response.status_code)
print("DEBUG: Response content snippet:")
print(response.text[:1000])  # Print only first 1000 characters


# Find citation stats: total citations, h-index, i10-index
data = soup.find_all("td", class_="gsc_rsb_std")

# Check that the expected elements were found
if len(data) >= 6:
    metrics = {
        "total_citations": data[0].text,
        "h_index": data[2].text,
        "i10_index": data[4].text,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    # Create the results directory if it doesn't exist
    results_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(results_dir, exist_ok=True)

    # Save raw metrics JSON
    with open(os.path.join(results_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    # Generate shields.io badge JSONs
    shield_citations = {
        "schemaVersion": 1,
        "label": "citations",
        "message": metrics["total_citations"],
        "color": "9cf",
        "labelColor": "f6f6f6"
    }

    shield_hindex = {
        "schemaVersion": 1,
        "label": "h_index",
        "message": metrics["h_index"],
        "color": "blueviolet",
        "labelColor": "f6f6f6"
    }

    with open(os.path.join(results_dir, "gs_data_shieldsio.json"), "w") as f:
        json.dump(shield_citations, f)

    with open(os.path.join(results_dir, "gs_data_h_shieldsio.json"), "w") as f:
        json.dump(shield_hindex, f)

    print("✅ Citation metrics scraped and saved.")
else:
    raise RuntimeError("❌ Failed to parse citation data from Google Scholar.")
