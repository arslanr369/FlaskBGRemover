from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

# Configure upload and processed folders
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Process the image
            output_path = os.path.join(app.config['PROCESSED_FOLDER'], f'processed_{file.filename}')
            with open(filepath, 'rb') as input_img:
                output_img = remove(input_img.read())
                with open(output_path, 'wb') as out:
                    out.write(output_img)
            
            return redirect(url_for('download_file', filename=f'processed_{file.filename}'))
    
    return render_template('index.html')

@app.route('/processed/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
