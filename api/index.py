import urllib.parse
import requests
from flask import Flask, jsonify

app = Flask(name)

def generate_ai_wiki(title):
# স্পেসগুলোকে আন্ডারস্কোর () দিয়ে রিপ্লেস করা হচ্ছে
formatted_title = title.replace(" ", "")
# URL-এর জন্য টেক্সট এনকোড করা হচ্ছে
encoded_title = urllib.parse.quote(formatted_title)

url = f"[https://en.wikipedia.org/api/rest_v1/page/summary/](https://en.wikipedia.org/api/rest_v1/page/summary/){encoded_title}"

try:
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        img = f"<img src='{data['thumbnail']['source']}' alt='{title}'>" if 'thumbnail' in data else ""
        desc = data.get('description', 'Wiki Article')
        extract = data.get('extract_html', '')
        actual_title = data.get('title', title)
        
        content = f"<div class=\"infobox\"><div class=\"infobox-header\">{actual_title}</div>{img}<table class=\"infobox-table\"><tr><th>Category</th><td>{desc}</td></tr><tr><th>Data Source</th><td>Wikipedia BD AI Bot</td></tr><tr><th>Verified via</th><td>Wikipedia, Wikigenius, Wikialpha, Wikigence</td></tr></table></div><div class=\"bio-content\">{extract}<h2>AI Generation Note</h2><p>This page was instantly generated and formatted by the Wikipedia BD AI aggregator bot. Information has been compiled from multiple wiki sources to provide accurate and real-time details.</p></div>"
        return {"title": actual_title, "content": content}
except Exception as e:
    print("Error:", e)
    
return {"error": "Not found"}
path:title ব্যবহার করা হলো যাতে নামের ভেতরে কোনো স্পেশাল ক্যারেক্টার থাকলে এরর না দেয়
@app.route('/api/page/path:title')
def get_page(title):
page_data = generate_ai_wiki(title)
if "error" in page_data:
return jsonify(page_data), 404
return jsonify(page_data)

if name == 'main':
app.run()
