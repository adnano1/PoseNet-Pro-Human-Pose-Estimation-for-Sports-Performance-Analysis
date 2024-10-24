# Split the data into training and validation sets
from sklearn.model_selection import train_test_split

train_images, val_images, train_keypoints, val_keypoints = train_test_split(
    preprocessed_images, preprocessed_keypoints, test_size=0.2, random_state=42)

# Train the model
history = model.fit(
    train_images, train_keypoints, 
    validation_data=(val_images, val_keypoints), 
    epochs=10, batch_size=32)

# Save the model after training
model.save('pose_estimation_model.h5')
