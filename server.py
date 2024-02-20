from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Direktori untuk menyimpan file buku
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully.'

@app.route('/books')
def list_books():
    books = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', books=books)

@app.route('/read/<filename>')
def read_book(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
