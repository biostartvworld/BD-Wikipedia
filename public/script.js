function loadPage(title) {
document.getElementById('createForm').style.display = 'none';
document.getElementById('content').style.display = 'block';
document.getElementById('pageTitle').innerText = "লোড হচ্ছে...";
document.getElementById('pageContent').innerHTML = "";

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

}

window.onload = () => loadPage('MD. Shinha Sarder');
