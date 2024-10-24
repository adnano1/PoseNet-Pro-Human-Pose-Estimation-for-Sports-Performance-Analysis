def preprocess_data(images, keypoints, img_size=(256, 256)):
    preprocessed_images = []
    preprocessed_keypoints = []

    for img, kp in zip(images, keypoints):
        # Resize the image
        resized_img = cv2.resize(img, img_size)
        
        # Normalize the keypoints
        kp[:, 0] = kp[:, 0] / img.shape[1] * img_size[0]  # Normalize x-coordinates
        kp[:, 1] = kp[:, 1] / img.shape[0] * img_size[1]  # Normalize y-coordinates
        
        preprocessed_images.append(resized_img)
        preprocessed_keypoints.append(kp)
    
    return np.array(preprocessed_images), np.array(preprocessed_keypoints)

preprocessed_images, preprocessed_keypoints = preprocess_data(images, keypoints)
print(f"Preprocessed image shape: {preprocessed_images.shape}")
print(f"Preprocessed keypoints shape: {preprocessed_keypoints.shape}")
