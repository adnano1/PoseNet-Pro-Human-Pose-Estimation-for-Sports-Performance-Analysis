import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential

# Load MobileNetV2 pre-trained model
base_model = MobileNetV2(input_shape=(256, 256, 3), include_top=False, weights='imagenet')

# Build custom model on top of MobileNetV2
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(512, activation='relu'),
    Dense(34)  # 17 keypoints * 2 (x, y) = 34
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Summary of the model
model.summary()
