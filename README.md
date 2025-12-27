# 🌍 Ethnicity Detection System
<p>A Flask-based web API that detects human ethnicity from facial images using a trained Convolutional Neural Network (CNN). Built with TensorFlow/Keras, OpenCV, and Flask, this system uses the UTKFace dataset for training and supports real-time inference via a simple HTTP endpoint.</p>
💡<strong>Ethical Note:</strong> This tool is for educational and research purposes only. Ethnicity is a social construct, and automated classification can be inaccurate or biased. Do <strong>not</strong> use in sensitive contexts (e.g., hiring, law enforcement, or surveillance).

## 📦 Features
- Accepts JPG/JPEG face images via HTTP POST
- Returns predicted ethnicity and confidence score
- Pre-trained CNN model (saved as ethnicity_cnn_model.h5)
- Cross-platform (Windows, macOS, Linux)
- Lightweight and easy to deploy

### Supported Ethnicity Labels
<ul>
   <li><code>White</code></li>
   <li><code>Black</code></li>
   <li><code>Asian</code></li>
   <li><code>Indian</code></li>
   <li><code>Others</code></li>
</ul>

## 🛠️ Tech Stack
- TensorFlow 2.x
-  Keras
-  Flask
-  OpenCV
-  NumPy
- Dataset: <a href="https://www.kaggle.com/datasets/jangedoo/utkface-new" target="_blank">UTKFace</a>

## 📁 Project Structure
<pre>ethnicity-detection/
├── ethnicity_cnn_model.h5      # Trained model (must be placed here)
├── app.py                      # Flask API server
├── requirements.txt            # Python dependencies
├── README.html                 # This file
</pre>

## 🚀 Setup & Installation
### 1. Prerequisites
<ul>
   <li>Python 3.8+</li>
   <li><code>pip</code> package manager</li>
   <li>Trained model file: <code>ethnicity_cnn_model.h5</code> (place in project root)</li>
</ul>

### 2. Create Virtual Environment</h3>
<div>Windows:
<span>.venv\Scripts\activate</span>
macOS/Linux:
<span>source .venv/bin/activate</span></div>

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Add Your Model</h3>
<p>Place <code>ethnicity_cnn_model.h5</code> in the project root directory.</p>

## ▶️ Running the API</h2>
Run this in the terminal  
```
python app.py
```
<p>You should see:</p>
<code>Loading model... <br>
Model loaded successfully! <br>
* Running on http://0.0.0.0:5000 <br> </code>
<p>The API is now live at <code>http://localhost:5000</code>.</p>

## 🧪 Testing the API
#### Endpoint: <code>POST /predict</code>
<p>Send a <strong>JPG</strong> image file via the <code>image</code> form field.</p>

#### Method 1: Using <code>curl</code> (Terminal)
```
curl -X POST -F "image=@your_face.jpg" http://localhost:5000/predict
```

#### Method 2: Using Insomnia / Postman
<ul>
<li><strong>URL:</strong> <code>http://localhost:5000/predict</code></li>
<li><strong>Method:</strong> <code>POST</code></li>
<li><strong>Body:</strong> <code>Multipart Form</code>
  <ul>
    <li>Key: <code>image</code></li>
    <li>Type: <code>File</code></li>
    <li>Value: Select a <code>.jpg</code> image</li>
  </ul>
</li>
</ul>

#### ✅ Success Response
<pre>{
"ethnicity": "Asian",
"confidence": 0.9821
}</pre>

#### ❌ Error Responses
<p><code>400</code>: "No image provided" or "Only JPG images are allowed"</p>
<p><code>500</code>: Internal error (e.g., corrupted image, model issue)</p>

## 📝 API Specification</h2>
<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Type</th>
    <th>Required</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>image</code></td>
    <td><code>file</code></td>
    <td>Yes</td>
    <td>JPG facial image (&lt;5 MB recommended)</td>
  </tr>
</tbody>
</table>
<p><strong>Note:</strong> PNG, BMP, GIF, etc. are <strong>rejected</strong> for consistency with training data.</p>

## 🧹 Cleanup & Safety
 <ul>
   <li>Uploaded images are <strong>never stored permanently</strong> — deleted immediately after prediction</li>
   <li>Filenames sanitized using <code>secure_filename()</code> to prevent path traversal attacks</li>
 </ul>

## 📦 Deployment Tips</h2>
<ul>
   <li>Use <strong>Gunicorn</strong> or <strong>uWSGI</strong> instead of Flask’s dev server</li>
   <li>Add file size limits (e.g., 5 MB max)</li>
   <li>Validate image content (not just extension)</li>
   <li>Serve behind <strong>Nginx</strong> with HTTPS</li>
   <li>Use <strong>Docker</strong> for containerization</li>
</ul>

## 📚 References
<ul>
   <li><strong>Dataset:</strong> <a href="https://www.kaggle.com/datasets/jangedoo/utkface-new" target="_blank">UTKFace on Kaggle</a></li>
   <li><strong>Model Architecture:</strong> Custom CNN (3 Conv layers + GlobalAvgPool + Dense)</li>
   <li><strong>Ethnicity Labels:</strong> As defined in UTKFace (0=White, 1=Black, 2=Asian, 3=Indian, 4=Others)</li>
</ul>

## 📜 License</h2>
<p>This project is for <strong>educational use only</strong>. No license granted for commercial deployment without ethical review.</p>
<pre>
💡 Tip: Always test with diverse, non-sensitive images. Never assume accuracy or fairness in biometric inference systems.
</pre>
