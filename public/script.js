function loadMainPage() {
document.getElementById('pageTitle').innerText = "Wikipedia BD";
document.getElementById('pageContent').innerHTML = "<p>Welcome to <strong>Wikipedia BD</strong>, the most advanced AI-powered wiki aggregation platform.</p><h2>About This Site</h2><ul><li><strong>Founder, CEO & Owner:</strong> MD. Shinha Sarder</li><li><strong>Technology:</strong> Wikipedia BD AI Aggregation Bot</li><li><strong>Data Sources:</strong> Wikipedia, Wikigenius, Wikialpha, Wikigence, EverybodyWiki</li></ul><p>Our proprietary AI bot dynamically fetches, verifies, and formats data from multiple wiki platforms across the internet to generate rich, infobox-styled pages instantly. Use the search bar above to generate any page.</p>";
}

function loadPage(title) {
document.getElementById('pageTitle').innerText = "AI Bot Generating Page...";
document.getElementById('pageContent').innerHTML = "<p>Wikipedia BD AI is securely collecting and formatting data from all sources...</p>";

fetch('/api/page/' + encodeURIComponent(title))
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('pageTitle').innerText = title;
            document.getElementById('pageContent').innerHTML = "<p>Our AI could not find sufficient data across Wikigenius, Wikipedia, or other sources to generate this page.</p>";
        } else {
            document.getElementById('pageTitle').innerText = data.title;
            document.getElementById('pageContent').innerHTML = data.content + '<div style="clear:both;"></div>';
        }
    })
    .catch(err => {
        document.getElementById('pageTitle').innerText = "Server Error";
        document.getElementById('pageContent').innerText = "Failed to connect to the Wikipedia BD AI Core.";
    });
}

function searchPage() {
const query = document.getElementById('searchInput').value;
if (query) {
loadPage(query);
}
}

window.onload = loadMainPage;

