import time
import re
import feedparser
import yaml
import email.utils
from pathlib import Path
from datetime import datetime

# Load RSS feed URLs from the config file
with open('config.yaml', 'r') as file:
    feeds = yaml.safe_load(file)['feeds']

# Fetch and parse each feed
for url in feeds:
    feed = feedparser.parse(url)
    
    # Process each news item in the feed
    for item in feed.entries:
        # Parse the published date to a datetime object
        pub_date = email.utils.parsedate_to_datetime(item.published)

        # Create a dictionary with the relevant information
        entry = {
            'timestamp': int(time.time()),
            'source': url,
            'published': pub_date.strftime('%Y-%m-%d'),
            'link': item.link,
            'title': item.title,
            'summary': item.summary
        }
        
        # Clean the title to remove unsafe characters
        safe_title = re.sub('[^a-zA-Z0-9 \n\.]', '', item.title)
        safe_title = safe_title.replace(' ', '_')[:50]  # Replace spaces with underscores and limit length

        # Generate a unique filename based on the cleaned title
        filename = f"rss_{pub_date.strftime('%Y-%m-%d')}_{safe_title}.yaml"
        
        # Check if file already exists, skip if it does
        if not (Path('data') / filename).exists():
            # Save the news item to a YAML file
            with open(Path('data') / filename, 'w') as file:
                yaml.dump(entry, file)
