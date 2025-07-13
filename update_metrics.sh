#!/bin/bash

cd ~/FANG/git/yw-fang.github.io || exit

# Run the scraper
python3 google_scholar_crawler/scrape_metrics.py

# Commit and push
git checkout google-scholar-stats
git add google_scholar_crawler/results/*.json
git commit -m "Update citation metrics (auto)" || echo "No changes to commit"
git push origin google-scholar-stats

git checkout master # back to master branch
