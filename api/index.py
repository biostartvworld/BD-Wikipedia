from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
manual_pages = {}

@app.route('/api/page/<title>', methods=['GET'])
def get_page(title):
    if title in manual_pages:
        return jsonify({"title": title, "content": manual_pages[title], "source": "BD Wikipedia"})
    
    wiki_url = f"https://bn.wikipedia.org/api/rest_v1/page/html/{title}"
    response = requests.get(wiki_url)
    
    if response.status_code == 200:
        return jsonify({"title": title, "content": response.text, "source": "Wikipedia"})
    else:
        return jsonify({"error": "Page not found"}), 404

@app.route('/api/page', methods=['POST'])
def create_page():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if title and content:
        manual_pages[title] = content
        return jsonify({"success": True, "title": title})
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run()
