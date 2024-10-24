import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET

# Path to dataset
dataset_dir = r'C:\Users\hashm\OneDrive\Desktop\PoseNet Pro Human Pose Estimation for Sports Performance Analysis\PoseEstimation\collage\0.jpg'
annotations_path = r'C:\Users\hashm\OneDrive\Desktop\PoseNet Pro Human Pose Estimation for Sports Performance Analysis\annotations.xml'

# Load and parse XML annotations
def parse_annotations(annotations_path):
    tree = ET.parse(annotations_path)
    root = tree.getroot()

    annotations = []
    
    for image in root.findall('image'):
        image_name = image.get('name')  # Assuming the image name is an attribute in the XML

        # Assuming keypoints are stored as child elements under 'image'
        keypoints = []
        for kp in image.findall('keypoint'):
            x = float(kp.get('x'))
            y = float(kp.get('y'))
            keypoints.append([x, y])
        
        annotations.append({
            'image_name': image_name,
            'keypoints': keypoints
        })
    
    return annotations

# Load images and keypoints
def load_data(annotations):
    images = []
    keypoints = []

    for item in annotations:
        image_path = os.path.join(dataset_dir, item['image_name'])
        image = cv2.imread(image_path)

        if image is not None:
            images.append(image)
            keypoints.append(np.array(item['keypoints']).reshape(-1, 2))  # Reshape keypoints (x, y)
    
    return images, keypoints

# Parse XML annotations and load data
annotations = parse_annotations(annotations_path)
images, keypoints = load_data(annotations)

# Check the result
print(f"Loaded {len(images)} images and {len(keypoints)} keypoints.")
