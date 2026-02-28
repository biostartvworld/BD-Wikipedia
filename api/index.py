import requests
from flask import Flask, request, jsonify

app = Flask(name)
manual_pages = {}

def get_owner_data():
return {
"title": "MD. Shinha Sarder",
"content": "<div class="infobox"><h3>MD. Shinha Sarder</h3><img src="" alt="MD. Shinha Sarder"><p><strong>Born:</strong> November 5, 2004</p><p><strong>Occupation:</strong> Developer, Programmer, Entrepreneur</p><p><strong>Education:</strong> Northern University of Business and Technology, Khulna</p><p><strong>Parents:</strong> MD. Lutfor Rahaman, Samima Sultana</p><p><strong>Projects:</strong> Biostar TV World</p></div><p>MD. Shinha Sarder is a CSE student, programmer, and the creator of BD Wikipedia and Biostar TV World. He is skilled in backend automation, knowledge panels management, and web development.</p>",
"source": "BD Wikipedia Owner"
}

@app.route('/api/page/<title>', methods=['GET'])
def get_page(title):
if title.lower() in ["owner", "developer", "md. shinha sarder"]:
return jsonify(get_owner_data())

@app.route('/api/page', methods=['POST'])
def create_page():
data = request.json
title = data.get('title')
content = data.get('content')
if title and content:
manual_pages[title] = content
return jsonify({"success": True, "title": title})
return jsonify({"error": "Invalid data"}), 400

if name == 'main':
app.run()
