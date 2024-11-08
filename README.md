# Flask Background Remover 🖼️✨  

![Flask](https://img.shields.io/badge/Flask-3.0.3-blue)  
![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen)  
![Rembg](https://img.shields.io/badge/Rembg-2.0.59-red)  

An elegant, simple, and powerful web application that allows you to remove the background from any image. Powered by **Flask** and **Rembg**, this app processes images directly in the browser, ensuring that you can get your results instantly without the hassle of manual editing.  

---

## Features 🚀  
- **Instant Background Removal**: Upload an image, and the app will automatically remove its background.  
- **Lightweight and Fast**: Built using Flask, ensuring minimal overhead and snappy performance.  
- **No File Storage**: Processed images are automatically downloaded to your device without being stored on the server.  
- **Modern Design**: Beautiful and responsive UI with gradient styling for a smooth user experience.  
- **Open Source**: Fully customizable and extendable.  

---

## Installation & Setup 🛠️  

### Prerequisites:  
- Python 3.9+  
- pip (Python package manager)  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/arslanr369/React-Python-BG-Remover.git  
cd Flask-BG-Remover  
```  

### Step 2: Create a Virtual Environment (Recommended)  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  

### Step 3: Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Step 4: Run the Application  
```bash  
python app.py  
```  
Navigate to `http://127.0.0.1:5000` in your web browser to use the app.  

---

## Usage 📸  

1. **Upload an Image**: Click the upload button and select your image.  
2. **Remove Background**: Hit the "Remove Background" button.  
3. **Download Processed Image**: The app will automatically download the image with the background removed.  

---

## Folder Structure 📂  

```plaintext  
Flask-BG-Remover/  
│  
├── app.py                  # Main application file  
├── templates/              # HTML templates  
│   └── index.html          # Main UI file  
├── static/  
│   └── styles.css          # Custom CSS styles  
├── venv/                   # Virtual environment (optional)  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  
```  

---

## Technologies Used 🛠️  
- **Flask**: A lightweight WSGI web application framework in Python.  
- **Rembg**: An AI-powered library for removing image backgrounds.  
- **HTML & CSS**: For building the responsive and modern user interface.  
- **Pillow**: Python Imaging Library for image manipulation.  

---

## Contributing 🤝  

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.  

---

## License 📜  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## Acknowledgments 🙌  
Special thanks to the contributors of **Flask** and **Rembg** for their amazing tools that made this project possible.  

---

**Made with 💖 by [Arslan Riaz](https://github.com/arslanr369)**  
