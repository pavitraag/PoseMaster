
# 🧘‍♀️ PoseMaster

**PoseMaster** is a Flask-based web application designed to detect and correct yoga poses using computer vision. Built using OpenCV and MediaPipe, the app analyzes real-time webcam input, compares body posture with predefined yoga poses, and provides helpful feedback to users to improve their form and alignment.

> 📸 Perform yoga poses in front of your camera and receive instant feedback!


## 🌟 Features

- 🧠 Real-time **pose detection** using MediaPipe
- 🎯 Automatic **pose accuracy scoring** based on body angles
- ✅ Visual **feedback on incorrect joints**
- 💡 **Reference pose matching** and tips for improvement
- 🔴 **Live webcam integration** for a seamless experience

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pavitraag/PoseMaster.git
cd PoseMaster
````

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then, open your browser and visit:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧰 Tech Stack

* **Framework**: Flask
* **Pose Detection**: MediaPipe
* **Computer Vision**: OpenCV
* **Language**: Python 3
* **Frontend**: HTML, CSS (Jinja2 templating)

---

## 📂 Project Structure

```
PoseMaster/
├── app.py                  # Main Flask application
├── reference_poses.json    # Reference joint angles for poses
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # UI template
├── static/
│   └── styles.css          # Styling (if applicable)
└── README.md
```

---

## 📸 How It Works

1. User allows webcam access via browser.
2. Pose is captured using OpenCV.
3. MediaPipe detects key body landmarks.
4. Angles between joints are calculated and compared to reference poses.
5. Visual and textual feedback is displayed in real-time.

---

## 🧘‍♀️ Supported Yoga Poses

* **Tadasana** (Mountain Pose)
* **Vrikshasana** (Tree Pose)
* **Trikonasana** (Triangle Pose)
* **Bhujangasana** (Cobra Pose)
* **Virabhadrasana** (Warrior Pose)

---

## 🧑‍💻 Contributing

We welcome contributions to make PoseMaster better!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/pose-feedback`)
3. Commit your changes (`git commit -m 'Add feedback on elbow angle'`)
4. Push to the branch (`git push origin feature/pose-feedback`)
5. Open a pull request

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

* [MediaPipe](https://github.com/google/mediapipe)
* [OpenCV](https://opencv.org/)
* Yoga pose datasets and posture analysis references
* Flask community for backend support

---

## 👩‍💻 Created By

**Pavitraa G**
🔗 [GitHub](https://github.com/pavitraag)
