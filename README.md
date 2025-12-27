🌍 Ethnicity Detection System
A Flask-based web API that detects human ethnicity from facial images using a trained Convolutional Neural Network (CNN). Built with TensorFlow/Keras, OpenCV, and Flask, this system uses the UTKFace dataset for training and supports real-time inference via a simple HTTP endpoint.

⚠️ Ethical Note: This tool is for educational and research purposes only. Ethnicity is a social construct, and automated classification can be inaccurate or biased. Do not use in sensitive contexts (e.g., hiring, law enforcement, or surveillance).

📦 Features
Accepts JPG/JPEG face images via HTTP POST
Returns predicted ethnicity and confidence score
Pre-trained CNN model (saved as ethnicity_cnn_model.h5)
Cross-platform (Windows, macOS, Linux)
Lightweight and easy to deploy
Supported Ethnicity Labels:

White
Black
Asian
Indian
Others
🛠️ Tech Stack
Machine Learning: TensorFlow 2.x, Keras
Backend: Flask
Image Processing: OpenCV, NumPy
Dataset: UTKFace
📁 Project Structure
123456
ethnicity-detection/
├── ethnicity_cnn_model.h5 # Trained model (must be placed here)
├── app.py # Flask API server
├── requirements.txt # Python dependencies
├── README.md
└── uploads/ # (Auto-created) Temporary image storage
🚀 Setup & Installation

1. Prerequisites
   Python 3.8+
   pip package manager
   Trained model file: ethnicity_cnn_model.h5
   (Place it in the project root)
2. Clone or Create Project Folder
   bash
   12
   mkdir ethnicity-detection
   cd ethnicity-detection
3. Create Virtual Environment (Recommended)
   bash
   1234567

# Windows

python -m venv .venv
.venv\Scripts\activate

# macOS/Linux

python3 -m venv .venv
source .venv/bin/activate 4. Install Dependencies
bash
1
🔍 Don’t have requirements.txt?
Run pip install flask tensorflow opencv-python numpy then pip freeze > requirements.txt.

5. Add Your Model
   Place your trained model file in the project root:

12
▶️ Running the API
Start the Flask server:

bash
1
You should see:

123
The API is now live at http://localhost:5000.

🧪 Testing the API
✅ Endpoint: POST /predict
Send a JPG/JPEG image file via the image form field.

Method 1: Using curl (Terminal)
bash
1
curl -X POST -F "image=@your_face.jpg" http://localhost:5000/predict
Method 2: Using Insomnia / Postman
URL: http://localhost:5000/predict
Method: POST
Body: Multipart Form
Key: image
Type: File
Value: Select a .jpg image
✅ Success Response
json
1234
{
"ethnicity": "Asian",
"confidence": 0.9821
}
❌ Error Responses
400: "No image provided" or "Only JPG/JPEG images are allowed"
500: Internal error (e.g., corrupted image, model issue)
📝 API Specification
Parameter
Type
Required
Description
image
file
Yes
JPG/JPEG facial image (<5 MB recommended)
📌 Note: PNG, BMP, GIF, etc. are rejected for consistency with training data.

🧹 Cleanup & Safety
Uploaded images are never stored permanently — they are saved temporarily and deleted immediately after prediction.
Filename is sanitized using secure_filename() to prevent path traversal attacks.
📦 Deployment Tips
For Production:
Use Gunicorn or uWSGI instead of Flask’s dev server
Add file size limits (e.g., 5 MB max)
Validate image content (not just extension)
Serve behind Nginx with HTTPS
Use Docker for containerization
Example Dockerfile (Optional)
Dockerfile
1234567891011
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ethnicity_cnn_model.h5 .
COPY app.py .

EXPOSE 5000

📚 References
Dataset: UTKFace on Kaggle
Model Architecture: Custom CNN (3 Conv layers + GlobalAvgPool + Dense)
Ethnicity Labels: As defined in UTKFace (0=White, 1=Black, 2=Asian, 3=Indian, 4=Others)
🙏 Acknowledgements
UTKFace dataset creators
TensorFlow & Flask open-source communities
📜 License
This project is for educational use only. No license granted for commercial deployment without ethical review.

💡 Tip: Always test with diverse, non-sensitive images. Never assume accuracy or fairness in biometric inference systems.
