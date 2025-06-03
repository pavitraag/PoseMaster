import cv2
import mediapipe as mp
import json
import os
import math

# Poses to extract (must match HTML poses list order)
poses = [
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\easy_pose\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\balasana\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\cat_pose\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\savasana\5.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\setu_bandhasana\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\dolphin_pose\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\ardha_uttanasana\0-0.png",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\tree\00000031.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\utkatasana\1.jpg",
    r"C:\Users\Sanpa Solutions\Downloads\majorproject\majorproject\dataset\train\baddha_konasana\1.jpg"
]

pose_dir = "poses"
output_json = "reference_angles.json"

# Joint triplets to calculate angles
joints_to_check = [
    [11, 13, 15],  # Left Elbow
    [12, 14, 16],  # Right Elbow
    [23, 25, 27],  # Left Knee
    [24, 26, 28],  # Right Knee
    [13, 11, 23],  # Left Shoulder
    [14, 12, 24]   # Right Shoulder
]

def calculate_angle(A, B, C):
    AB = (A[0] - B[0], A[1] - B[1])
    CB = (C[0] - B[0], C[1] - B[1])
    dot_product = AB[0]*CB[0] + AB[1]*CB[1]
    mag_AB = math.sqrt(AB[0]**2 + AB[1]**2)
    mag_CB = math.sqrt(CB[0]**2 + CB[1]**2)
    if mag_AB == 0 or mag_CB == 0:
        return None
    angle_rad = math.acos(dot_product / (mag_AB * mag_CB))
    return angle_rad * 180 / math.pi

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

reference_data = []

for filename in poses:
    img_path = os.path.join(pose_dir, filename)
    image = cv2.imread(img_path)
    if image is None:
        print(f"[ERROR] Could not load image: {img_path}")
        reference_data.append([None]*len(joints_to_check))
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = pose.process(image_rgb)

    if not result.pose_landmarks:
        print(f"[WARNING] No pose detected in: {filename}")
        reference_data.append([None]*len(joints_to_check))
        continue

    landmarks = result.pose_landmarks.landmark
    image_height, image_width = image.shape[:2]

    landmark_points = [(int(lm.x * image_width), int(lm.y * image_height)) for lm in landmarks]

    angles = []
    for a, b, c in joints_to_check:
        try:
            A, B, C = landmark_points[a], landmark_points[b], landmark_points[c]
            angle = calculate_angle(A, B, C)
            angles.append(round(angle, 2) if angle is not None else None)
        except IndexError:
            angles.append(None)

    reference_data.append(angles)

pose.close()

# Save to JSON
with open(output_json, "w") as f:
    json.dump(reference_data, f, indent=2)

print(f"[SUCCESS] Angles written to {output_json}")
