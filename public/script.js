function loadPage(title) {
    document.getElementById('createForm').style.display = 'none';
    document.getElementById('content').style.display = 'block';
    document.getElementById('pageTitle').innerText = "লোড হচ্ছে...";
    document.getElementById('pageContent').innerHTML = "";

    fetch(`/api/page/${title}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('pageTitle').innerText = title;
                document.getElementById('pageContent').innerHTML = "এই পাতাটি পাওয়া যায়নি। আপনি চাইলে নতুন তৈরি করতে পারেন।";
            } else {
                document.getElementById('pageTitle').innerText = data.title;
                document.getElementById('pageContent').innerHTML = data.content + '<div class="clear"></div>';
            }
        })
        .catch(err => {
            document.getElementById('pageTitle').innerText = "ত্রুটি";
            document.getElementById('pageContent').innerText = "সার্ভারের সাথে সংযোগ করা যায়নি।";
        });
}

function searchPage() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        loadPage(query);
    }
}

function showCreateForm() {
    document.getElementById('content').style.display = 'none';
    document.getElementById('createForm').style.display = 'flex';
}

function submitPage() {
    const title = document.getElementById('newTitle').value;
    const content = document.getElementById('newContent').value;

    if (title && content) {
        fetch('/api/page', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, content })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loadPage(data.title);
            }
        });
    }
}

window.onload = () => loadPage('MD. Shinha Sarder');
