# 🌿 Cassava Leaf Disease Detection using EfficientNetB3

This project uses a deep learning model based on **EfficientNetB3** to classify cassava leaf diseases into 5 categories with high accuracy. It includes an end-to-end pipeline from preprocessing to deployment using a Flask web interface.

---

## 📊 Model Performance

- **Model Architecture:** EfficientNetB3
- **Input Size:** 224x224 RGB images
- **Final Validation Accuracy:** **92.85%**
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam

---

## 🦠 Disease Categories

1. Cassava Bacterial Blight (CBB)  
2. Cassava Brown Streak Disease (CBSD)  
3. Cassava Green Mottle (CGM)  
4. Cassava Mosaic Disease (CMD)  
5. Healthy

---

## 🚀 Web App Features

- Upload a single image or select a folder of test images
- Batch prediction supported
- Predictions shown with confidence scores
- Beautiful agricultural-style UI with blurred background
- Built with Flask and TensorFlow/Keras

---

## 🧪 Dataset

- Source: [Cassava Leaf Disease Kaggle Competition](https://www.kaggle.com/competitions/cassava-leaf-disease-classification)
- Format: JPEG images + JSON labels
- Download the Model File
The trained model file (best_model.keras) is not included in this repository due to file size limits.

Please download it from Dropbox:
https://www.dropbox.com/scl/fi/6hyouzu048ar2muuacf5l/best_model.keras?rlkey=q39lhe6tc2rdfvue4r2vozf9c&st=b8ud7dch&dl=0

After downloading, place the file in the root directory of this project before running the app.
---

## 🛠️ Project Structure

```
Cassava/
├── app.py                    # Flask app
├── best_model.keras          # Trained EfficientNetB3 model
├── test_images/              # Test image folders
│   └── set1/
│       └── *.jpg
├── templates/
│   └── batch_results.html    # Web UI
├── static/                   # Static files (if needed)
│   └── style.css             # (Optional) Custom styling
├── requirements.txt          # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Usage

```bash
# Clone repo
git clone https://github.com/Vedant-k07/Cassava-Leaf-Detection-using-EFFICIENTNETB3
cd Cassava-Leaf-Detection-using-EFFICIENTNETB3

# Create virtual env
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ✅ Future Improvements

- Add support for mobile or edge deployment (e.g., TensorFlow Lite)
- Add image augmentation visualization
- Dockerize the entire pipeline
- Deploy on cloud (AWS / Heroku / Streamlit Cloud)

---

## 👨‍💻 Author

**Vedant Kumbhar**  
B.Tech CSE (AIML) | LTCE | [@Vedant-k07](https://github.com/Vedant-k07)

---

## 📄 License

MIT License – Feel free to use or adapt this project.
