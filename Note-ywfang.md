For getting citation data, not only do as the instructions in the README.md.
But also we need go to setting, repository - settings - code and automation -
Actions - general - Workflow permissions, choose the 'read and write
permission'

In addition, sometimes the build cannot regoginize the git user.name and
user.email properly, we can add several lines to specify your own user.name and
user.emai in the ./.github/workflows/google_scholar_crawler.yaml 

Lastly, you need to updat the badge URL. in my case, it is:

<a href='https://scholar.google.com/citations?user=6NU1KPQAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https://cdn.jsdelivr.net/gh/yw-fang/yw-fang.github.io@google-scholar-stats/gs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

In this code, the url parameter specifies the location of the JSON file containing the citation data. The part of the URL after @ specifies the name of the branch where the JSON file is located. Assuming that you are still using the "google-scholar-stats" branch for the JSON file, the updated URL would look like this:

url=https://cdn.jsdelivr.net/gh/yw-fang/yw-fang.github.io@google-scholar-stats/gs_data_shieldsio.json

Once you have updated the URL in the Markdown code, commit the changes to your repository and the badge should now display the updated citation data.
