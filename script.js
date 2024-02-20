// script.js
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(message => {
        alert(message);
        location.reload(); // Refresh halaman setelah unggahan berhasil
    })
    .catch(error => console.error('Error:', error));
});
