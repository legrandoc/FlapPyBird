import math
import os

import pygame

# Initialize Pygame
pygame.init()

# Settings
SIZE = 64  # Size of the explosion image (64x64 pixels)
NUM_FRAMES = 5
COLORS = [
    (255, 200, 50),
    (255, 140, 40),
    (255, 80, 30),
    (200, 40, 20),
    (150, 30, 10),
]  # Orange to red gradient


def create_explosion_frame(
    size: int, frame: int, max_frames: int
) -> pygame.Surface:
    """Create a single explosion frame"""
    surface = pygame.Surface((size, size), pygame.SRCALPHA)

    # Calculate the radius for this frame
    max_radius = size // 2 - 4
    radius = int(max_radius * (1 + frame) / max_frames)

    # Calculate alpha (fade out)
    alpha = 255 * (1 - frame / max_frames)

    # Get color for this frame
    color = COLORS[frame]

    # Draw the main circle
    center = (size // 2, size // 2)
    pygame.draw.circle(surface, (*color, alpha), center, radius)

    # Add some particles
    num_particles = 8
    for i in range(num_particles):
        angle = 2 * math.pi * i / num_particles
        distance = radius * 0.8
        x = center[0] + math.cos(angle) * distance
        y = center[1] + math.sin(angle) * distance
        particle_radius = max(2, radius // 4)
        pygame.draw.circle(
            surface, (*color, alpha), (int(x), int(y)), particle_radius
        )

    return surface


def main():
    # Create assets/sprites directory if it doesn't exist
    os.makedirs("assets/sprites", exist_ok=True)

    # Generate explosion frames
    for i in range(NUM_FRAMES):
        # Create the frame
        surface = create_explosion_frame(SIZE, i, NUM_FRAMES)

        # Save the frame
        filename = f"assets/sprites/explosion{i+1}.png"
        pygame.image.save(surface, filename)
        print(f"Generated {filename}")


if __name__ == "__main__":
    main()
    pygame.quit()
