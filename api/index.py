import os
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)
db = client.bd_wikipedia
pages_collection = db.manual_pages

def get_owner_data():
    return {
        "title": "MD. Shinha Sarder",
        "content": """
        <div class="infobox">
            <h3>MD. Shinha Sarder</h3>
            <img src="https://via.placeholder.com/250x250.png?text=MD.+Shinha+Sarder" alt="MD. Shinha Sarder">
            <p><strong>Born:</strong> November 5, 2004</p>
            <p><strong>Occupation:</strong> Developer, Programmer, Entrepreneur</p>
            <p><strong>Education:</strong> Northern University of Business and Technology, Khulna</p>
            <p><strong>Parents:</strong> MD. Lutfor Rahaman, Samima Sultana</p>
            <p><strong>Projects:</strong> Biostar TV World</p>
        </div>
        <p>MD. Shinha Sarder is a CSE student, programmer, and the creator of BD Wikipedia and Biostar TV World. He is skilled in backend automation, knowledge panels management, and AI image generation.</p>
        """,
        "source": "BD Wikipedia Owner"
    }

@app.route('/api/page/<title>', methods=['GET'])
def get_page(title):
    if title.lower() in ["owner", "developer", "md. shinha sarder"]:
        return jsonify(get_owner_data())
    
    manual_page = pages_collection.find_one({"title": {"$regex": f"^{title}$", "$options": "i"}})
    if manual_page:
        return jsonify({
            "title": manual_page["title"],
            "content": manual_page["content"],
            "source": "BD Wikipedia"
        })
    
    wiki_url = f"https://bn.wikipedia.org/api/rest_v1/page/summary/{title}"
    response = requests.get(wiki_url)
    
    if response.status_code == 200:
        data = response.json()
        img_html = f"<img src='{data['thumbnail']['source']}' width='250'>" if 'thumbnail' in data else ""
        extract = data.get('extract_html', '')
        
        content = f"""
        <div class="infobox">
            <h3>{data.get('title', title)}</h3>
            {img_html}
        </div>
        <div>{extract}</div>
        """
        return jsonify({"title": data.get('title', title), "content": content, "source": "Wikipedia API"})
    else:
        return jsonify({"error": "Page not found"}), 404

@app.route('/api/page', methods=['POST'])
def create_page():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if title and content:
        pages_collection.update_one(
            {"title": title},
            {"$set": {"title": title, "content": content}},
            upsert=True
        )
        return jsonify({"success": True, "title": title})
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run()
