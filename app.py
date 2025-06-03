'''from flask import Flask, send_file, send_from_directory, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import json
import mediapipe as mp
import os

app = Flask(__name__, template_folder='.')
CORS(app)

# Initialize MediaPipe pose detector
mp_pose = mp.solutions.pose
pose_detector = mp_pose.Pose(static_image_mode=True)

# Load reference landmarks (precomputed and stored in a JSON file)
with open('reference_landmarks.json', 'r') as f:
    reference_landmarks = json.load(f)

def extract_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose_detector.process(image_rgb)  # Use pose_detector, not pose
    if results.pose_landmarks:
        return [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]
    return None

def compare_landmarks(ref, current):
    if not ref or not current or len(ref) != len(current):
        return 0
    distances = [np.linalg.norm(np.array(r) - np.array(c)) for r, c in zip(ref, current)]
    similarity = max(0, 1 - np.mean(distances))  # Similarity score between 0 and 1
    return similarity

@app.route('/pose-feedback', methods=['POST'])
def pose_feedback():
    data = request.json
    image_data = base64.b64decode(data['image'].split(',')[1])
    pose_name = data['pose_name']

    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    current = extract_landmarks(frame)
    reference = reference_landmarks.get(pose_name)

    similarity = compare_landmarks(reference, current)
    return jsonify({'similarity': round(similarity * 100, 2)})

# Serve pages and images

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/browser')
def browser():
    return send_file('browser.html')


@app.route('/xception')
def xception():
    return send_file('xception.html')

@app.route('/vgg16')
def vgg16():
    return send_file('vgg16.html')

@app.route('/efficientnet')
def efficientnet():
    return send_file('efficientnet.html')

@app.route('/densenet')
def densenet():
    return send_file('densenet.html')

@app.route('/yoga')
def yoga():
    return send_file('yoga.html')


@app.route('/pose')
def pose():
    return send_file('pose.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/<filename>')
def serve_image(filename):
    return send_file(filename)

@app.route('/poses/<filename>')
def send_pose_image(filename):
    return send_from_directory('static/poses', filename)

if __name__ == '__main__':
    app.run(debug=True)

    '''





from flask import Flask, send_file, send_from_directory, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import json
import mediapipe as mp
import os

app = Flask(__name__, template_folder='.')
CORS(app)

# Initialize MediaPipe pose detector (reuse per request is safer)
mp_pose = mp.solutions.pose

# Load reference landmarks (make sure this file exists and is valid JSON)
try:
    with open('reference_landmarks.json', 'r') as f:
        reference_landmarks = json.load(f)
except Exception as e:
    print(f"Error loading reference_landmarks.json: {e}")
    reference_landmarks = {}

def extract_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    with mp_pose.Pose(static_image_mode=True) as pose_detector:
        results = pose_detector.process(image_rgb)
        if results.pose_landmarks:
            return [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]
    return None

def compare_landmarks(ref, current):
    if not ref or not current or len(ref) != len(current):
        return 0
    distances = [np.linalg.norm(np.array(r) - np.array(c)) for r, c in zip(ref, current)]
    similarity = max(0, 1 - np.mean(distances))  # score between 0 and 1
    return similarity

@app.route('/pose-feedback', methods=['POST'])
def pose_feedback():
    try:
        data = request.json
        if 'image' not in data or 'pose_name' not in data:
            return jsonify({'error': 'Missing image or pose_name'}), 400

        # Expect base64 image string, optionally with data header
        image_b64 = data['image']
        if ',' in image_b64:
            image_b64 = image_b64.split(',')[1]

        image_data = base64.b64decode(image_b64)
        nparr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({'error': 'Invalid image data'}), 400

        current = extract_landmarks(frame)
        reference = reference_landmarks.get(data['pose_name'])

        if reference is None:
            return jsonify({'error': f'Reference pose "{data["pose_name"]}" not found'}), 404

        similarity = compare_landmarks(reference, current)
        return jsonify({'similarity': round(similarity * 100, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Static routes for HTML pages and images below...
@app.route('/')
def index():
    return send_file('index.html')

@app.route('/browser')
def browser():
    return send_file('browser.html')

@app.route('/xception')
def xception():
    return send_file('xception.html')

@app.route('/vgg16')
def vgg16():
    return send_file('vgg16.html')

@app.route('/efficientnet')
def efficientnet():
    return send_file('efficientnet.html')

@app.route('/densenet')
def densenet():
    return send_file('densenet.html')

@app.route('/yoga')
def yoga():
    return send_file('yoga.html')

@app.route('/fitness')
def fitness():
    return send_file('fitness.html')

@app.route('/pose')
def pose():
    return send_file('pose.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/<filename>')
def serve_image(filename):
    if os.path.isfile(filename):
        return send_file(filename)
    return '', 404

@app.route('/poses/<filename>')
def send_pose_image(filename):
    return send_from_directory('static/poses', filename)

if __name__ == '__main__':
    app.run(debug=True)





