import math

# Function to calculate angle between three keypoints (e.g., shoulder, elbow, wrist)
def calculate_angle(a, b, c):
    a = np.array(a)  # First joint
    b = np.array(b)  # Second joint (elbow)
    c = np.array(c)  # Third joint
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

# Example: Calculate elbow angle (between shoulder, elbow, wrist)
elbow_angle = calculate_angle(predicted_keypoints[5], predicted_keypoints[7], predicted_keypoints[9])  # Assume keypoint indexes
print(f'Elbow Angle: {elbow_angle}')
