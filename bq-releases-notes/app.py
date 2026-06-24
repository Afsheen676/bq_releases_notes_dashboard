import os
import re
import xml.etree.ElementTree as ET
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Feed URL
FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "cached_feed.xml")

def parse_feed_content(entry_title, entry_date, entry_link, html_content):
    # Split content by <h3> headers
    pattern = re.compile(r'<h3>(.*?)</h3>(.*?)(?=<h3>|$)', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(html_content)
    
    updates = []
    if not matches:
        # Fallback if no h3 is found
        updates.append({
            "date": entry_title,
            "category": "General",
            "content": html_content.strip(),
            "link": entry_link,
            "id": re.sub(r'[^a-zA-Z0-9]', '_', f"{entry_title}_general")
        })
        return updates
        
    for idx, (category, content) in enumerate(matches):
        category = category.strip()
        content = content.strip()
        
        # Create a unique ID for frontend selection
        safe_title = re.sub(r'[^a-zA-Z0-9]', '_', entry_title)
        safe_cat = re.sub(r'[^a-zA-Z0-9]', '_', category)
        unique_id = f"{safe_title}_{safe_cat}_{idx}"
        
        updates.append({
            "date": entry_title,
            "category": category,
            "content": content,
            "link": f"{entry_link}#{category.replace(' ', '_')}_{idx}",
            "id": unique_id
        })
    return updates

def load_xml_data():
    xml_data = None
    # Try fetching from the live feed
    try:
        response = requests.get(FEED_URL, timeout=8)
        if response.status_code == 200:
            xml_data = response.text
            # Cache the successful response
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                f.write(xml_data)
    except Exception as e:
        print(f"Network fetch failed: {e}. Attempting cache fallback...")

    # Fallback to cache if network fetch failed
    if not xml_data and os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                xml_data = f.read()
            print("Loaded release notes from local cache.")
        except Exception as e:
            print(f"Failed to read cache file: {e}")
            
    return xml_data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/releases")
def get_releases():
    xml_data = load_xml_data()
    if not xml_data:
        return jsonify({
            "error": "Failed to fetch release notes and no local cache was found."
        }), 500
        
    try:
        root = ET.fromstring(xml_data)
        # Atom namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        all_updates = []
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text
            link_elem = entry.find('atom:link', ns)
            link = link_elem.attrib.get('href') if link_elem is not None else ""
            
            content_elem = entry.find('atom:content', ns)
            if content_elem is not None:
                html_content = content_elem.text or ""
                entry_updates = parse_feed_content(title, title, link, html_content)
                all_updates.extend(entry_updates)
                
        return jsonify({"updates": all_updates})
    except Exception as e:
        return jsonify({"error": f"Failed to parse XML data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
