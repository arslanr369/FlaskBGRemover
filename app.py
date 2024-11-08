from flask import Flask, request, render_template, send_file, redirect, url_for
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Process the image in memory
            input_img = Image.open(file.stream).convert('RGBA')
            input_bytes = io.BytesIO()
            input_img.save(input_bytes, format='PNG')
            input_bytes.seek(0)

            # Remove background
            output_bytes = remove(input_bytes.read())
            
            # Create a downloadable file in memory
            output_file = io.BytesIO(output_bytes)
            output_file.seek(0)

            # Serve the file as a download response
            return send_file(
                output_file,
                mimetype='image/png',
                as_attachment=True,
                download_name='background_removed.png'
            )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
