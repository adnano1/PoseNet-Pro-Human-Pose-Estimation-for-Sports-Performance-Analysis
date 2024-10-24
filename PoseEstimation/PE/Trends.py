import matplotlib.pyplot as plt

def plot_angle_trend(angles):
    plt.plot(angles, label="Elbow Angle")
    plt.xlabel('Frame')
    plt.ylabel('Angle (degrees)')
    plt.legend()
    plt.show()

# Assuming elbow angles were calculated for every frame
elbow_angles = [120, 135, 150, 160, 140, 130]  # Example values
plot_angle_trend(elbow_angles)
