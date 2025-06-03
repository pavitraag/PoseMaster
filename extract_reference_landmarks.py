import os
import cv2
import json
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

input_dir = r'D:\majorproject\dataset\train' 
landmarks_dict = {}

for class_name in sorted(os.listdir(input_dir)):
    class_path = os.path.join(input_dir, class_name)
    if not os.path.isdir(class_path): continue

    for image_file in sorted(os.listdir(class_path)):
        img_path = os.path.join(class_path, image_file)
        image = cv2.imread(img_path)
        if image is None: continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            landmarks = [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]
            landmarks_dict[class_name] = landmarks
            break  # Only take the first image per class

with open('reference_landmarks.json', 'w') as f:
    json.dump(landmarks_dict, f)
