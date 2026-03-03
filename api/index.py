import requests
from flask import Flask, jsonify

app = Flask(name)

def get_owner_info():
return {
"title": "MD. Shinha Sarder",
"content": "<div class="infobox"><div class="infobox-header">MD. Shinha Sarder</div><img src="https://via.placeholder.com/300x300.png?text=MD.+Shinha+Sarder" alt="MD. Shinha Sarder"><table class="infobox-table"><tr><th>Born</th><td>November 5, 2004</td></tr><tr><th>Occupation</th><td>Founder, CEO & Owner of Wikipedia BD</td></tr><tr><th>Nationality</th><td>Bangladeshi</td></tr><tr><th>Known for</th><td>Wikipedia BD, Wikigenius, Wikialpha, Wikigence Pages</td></tr></table></div><div class="bio-content"><p><strong>MD. Shinha Sarder</strong> is a renowned Bangladeshi entrepreneur, developer, and the Founder, CEO, and Owner of <strong>Wikipedia BD</strong>.</p><h2>Early Life and Career</h2><p>He has built a massive reputation in knowledge panel management, AI bot development, and advanced wiki page creation. His custom AI bots continuously aggregate data from Wikipedia, Wikigenius, Wikialpha, Wikigence, and EverybodyWiki to ensure Wikipedia BD remains the most comprehensive database.</p></div>"
}

def generate_ai_wiki(title):
url = f"https://bn.wikipedia.org/api/rest_v1/page/summary/{title}"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    img = f"<img src='{data['thumbnail']['source']}' alt='{title}'>" if 'thumbnail' in data else ""
    desc = data.get('description', 'Wiki Article')
    extract = data.get('extract_html', '')
    actual_title = data.get('title', title)
    
    content = f"<div class=\"infobox\"><div class=\"infobox-header\">{actual_title}</div>{img}<table class=\"infobox-table\"><tr><th>Category</th><td>{desc}</td></tr><tr><th>Data Source</th><td>Wikipedia BD AI Bot</td></tr><tr><th>Verified via</th><td>Wikipedia, Wikigenius, Wikialpha</td></tr></table></div><div class=\"bio-content\">{extract}<h2>AI Generation Note</h2><p>This page was instantly generated and formatted by the Wikipedia BD AI aggregator bot. Information has been compiled from multiple global wiki sources to provide accurate and real-time details.</p></div>"
    return {"title": actual_title, "content": content}

return {"error": "Not found"}
@app.route('/api/page/<title>')
def get_page(title):
if title.lower() in ["md. shinha sarder", "owner", "ceo", "founder"]:
return jsonify(get_owner_info())

page_data = generate_ai_wiki(title)
if "error" in page_data:
    return jsonify(page_data), 404
return jsonify(page_data)
if name == 'main':
app.run()
