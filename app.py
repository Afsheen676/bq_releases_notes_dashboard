from flask import Flask, render_template, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

# UPDATED: Correct BigQuery Release Notes Feed URL
FEED_URL = "https://cloud.google.com/feeds/bigquery-release-notes.xml"

def fetch_notes():
    try:
        print("Fetching feed...")
        r = requests.get(FEED_URL, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        print(f"Status: {r.status_code}")
        r.raise_for_status()
        
        root = ET.fromstring(r.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        notes = []
        
        for entry in root.findall('atom:entry', ns)[:50]:
            title = entry.find('atom:title', ns)
            summary = entry.find('atom:summary', ns)
            published = entry.find('atom:published', ns)
            link = entry.find('atom:link', ns)
            
            notes.append({
                'title': title.text if title is not None else "No title",
                'summary': summary.text if summary is not None else "No summary",
                'published': published.text if published is not None else "",
                'link': link.get('href') if link is not None else "#"
            })
        print(f"Found {len(notes)} notes")
        return notes
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes')
def get_notes():
    return jsonify(fetch_notes())

@app.route('/api/refresh')
def refresh():
    return jsonify(fetch_notes())

if __name__ == '__main__':
    app.run(debug=True, port=5000)