# Load the saved model
model = tf.keras.models.load_model('pose_estimation_model.h5')

def predict_pose(image):
    # Preprocess the input image (resize and scale)
    img = cv2.resize(image, (256, 256))
    img = np.expand_dims(img, axis=0) / 255.0

    # Predict keypoints
    keypoints = model.predict(img).reshape(-1, 2)

    # Scale the keypoints back to original image size
    keypoints[:, 0] *= image.shape[1] / 256
    keypoints[:, 1] *= image.shape[0] / 256

    return keypoints

# Test pose prediction on a new image
test_image = cv2.imread('path_to_test_image.jpg')
predicted_keypoints = predict_pose(test_image)

# Visualize predicted keypoints on the test image
for (x, y) in predicted_keypoints:
    cv2.circle(test_image, (int(x), int(y)), 5, (0, 255, 0), -1)

cv2.imshow('Pose Estimation', test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

