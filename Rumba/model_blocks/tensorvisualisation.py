import torch
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Create your [3, 4, 5] tensor with random values
# Imagine this as 3 separate 4x5 images
tensor_3d = torch.rand(3, 4, 5)

fig, ax = plt.subplots()
im = ax.imshow(tensor_3d[0], cmap='viridis', interpolation='nearest')
plt.colorbar(im)

def update(frame):
    # Update the image data for each 'slice' (0, 1, 2)
    im.set_array(tensor_3d[frame])
    ax.set_title(f"Viewing Slice: {frame} | Shape: {tensor_3d[frame].shape}")
    return [im]

# 2. Create the animation
ani = animation.FuncAnimation(fig, update, frames=3, interval=1000, blit=True)

plt.show()