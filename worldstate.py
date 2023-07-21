from flask import Flask, request
import os
import yaml
import glob
from datetime import datetime

app = Flask('worldstate')

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', default = None, type = str)
    date = request.args.get('date', default = None, type = str)

    # Get a list of all the .yaml files
    files = glob.glob("data/*.yaml")

    results = []

    # Search each file
    for filename in files:
        with open(filename, 'r') as file:
            entry = yaml.safe_load(file)

            # If a date was provided, skip entries from other dates
            if date and entry['published'] != date:
                continue

            # If a keyword was provided, skip entries that don't contain the keyword
            if keyword and keyword.lower() not in entry['title'].lower() and keyword.lower() not in entry['summary'].lower():
                continue

            results.append(entry)

    return {'results': results}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
