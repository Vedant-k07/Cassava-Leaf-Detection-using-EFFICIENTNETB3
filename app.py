import os
from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Ensure our test_folders dir exists (absolute path)
BASE_TEST_FOLDER = os.path.join(app.root_path, 'static', 'test_folders')
os.makedirs(BASE_TEST_FOLDER, exist_ok=True)

# Load model
model = tf.keras.models.load_model('best_model.keras')

# Cassava class names
class_names = [
    'Cassava Bacterial Blight',
    'Cassava Brown Streak Disease',
    'Cassava Green Mottle',
    'Cassava Mosaic Disease',
    'Healthy'
]

def preprocess_image(path):
    img = Image.open(path).convert('RGB').resize((224, 224))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)

@app.route('/', methods=['GET', 'POST'])
def predict_from_folder():
    # Use absolute path to list directories
    folders = [
        name for name in os.listdir(BASE_TEST_FOLDER)
        if os.path.isdir(os.path.join(BASE_TEST_FOLDER, name))
    ]

    selected = None
    results = []

    if request.method == 'POST':
        selected = request.form.get('folder')
        folder_path = os.path.join(BASE_TEST_FOLDER, selected)

        for fn in os.listdir(folder_path):
            if fn.lower().endswith(('.jpg', '.jpeg', '.png')):
                full = os.path.join(folder_path, fn)
                batch = preprocess_image(full)
                preds = model.predict(batch)
                idx = int(np.argmax(preds))
                conf = float(np.max(preds)) * 100

                results.append({
                    'filename': fn,
                    'image_path': f'/static/test_folders/{selected}/{fn}',
                    'prediction': class_names[idx],
                    'confidence': f"{conf:.2f}%"
                })

    return render_template(
        'batch_results.html',
        folders=folders,
        selected=selected,
        results=results
    )

if __name__ == '__main__':
    app.run(debug=True)
