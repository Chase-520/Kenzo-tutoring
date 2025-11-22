from PIL import Image
import pygame

class GIF:
    def __init__(self, filepath, scale=1.0, flip_x=False, flip_y=False):
        """Load a GIF or image and extract frames into Pygame surfaces."""
        self.filepath = filepath
        self.frames = []
        self.frame_durations = []

        self.scale = scale
        self.flip_x = flip_x
        self.flip_y = flip_y

        # Load image with Pillow
        pil_image = Image.open(filepath)
        self.is_animated = getattr(pil_image, "is_animated", False)
        
        try:
            while True:
                frame = pil_image.convert("RGBA")
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()

                pygame_image = pygame.image.fromstring(data, size, mode)

                # ✅ Apply transformations (flip + scale)
                if self.flip_x or self.flip_y:
                    pygame_image = pygame.transform.flip(pygame_image, self.flip_x, self.flip_y)

                if self.scale != 1.0:
                    new_size = (int(size[0] * self.scale), int(size[1] * self.scale))
                    pygame_image = pygame.transform.smoothscale(pygame_image, new_size)

                self.frames.append(pygame_image)

                # For static images, use a default duration
                duration = pil_image.info.get('duration', 100) if self.is_animated else 100
                self.frame_durations.append(duration)

                pil_image.seek(pil_image.tell() + 1)
        except EOFError:
            pass

        self.current_frame = 0
        self.time_accumulator = 0

    def update(self, dt=100):
        """Update frame based on elapsed time (dt in milliseconds). Only animates if actually animated."""
        if not self.frames or not self.is_animated:
            return

        self.time_accumulator += dt
        if self.current_frame < len(self.frames):
            if self.time_accumulator >= self.frame_durations[self.current_frame]:
                self.time_accumulator = 0
                self.current_frame += 1

    def get_frame(self):
        """Return the current frame surface."""
        if not self.frames:
            return None
            
        if self.is_animated:
            if self.current_frame < len(self.frames):
                return self.frames[self.current_frame]
            return self.frames[-1]  # Return last frame if animation ended
        else:
            # For static images, always return the first (and only) frame
            return self.frames[0]

    def reset_index(self):
        """Reset animation to first frame."""
        self.current_frame = 0
        self.time_accumulator = 0

    def reached_last_frame(self):
        """Check if animation reached the last frame. For static images, always returns False."""
        if not self.is_animated:
            return False
        return self.current_frame >= len(self.frames)
    
    def set_transform(self, scale=None, flip_x=None, flip_y=None):
        """Change transformation settings and reapply them to all frames."""
        if scale is not None:
            self.scale = scale
        if flip_x is not None:
            self.flip_x = flip_x
        if flip_y is not None:
            self.flip_y = flip_y

        # Reapply transformations to all frames
        transformed = []
        for frame in self.frames:
            img = frame
            if self.flip_x or self.flip_y:
                img = pygame.transform.flip(img, self.flip_x, self.flip_y)
            if self.scale != 1.0:
                size = img.get_size()
                new_size = (int(size[0] * self.scale), int(size[1] * self.scale))
                img = pygame.transform.smoothscale(img, new_size)
            transformed.append(img)
        self.frames = transformed

    def set_transparency(self, alpha):
        """Set transparency (alpha) for all frames. Alpha range: 0 (transparent) to 255 (opaque)."""
        if not self.frames:
            return
            
        alpha = max(0, min(255, alpha))  # Clamp alpha to valid range
        
        # Create new frames with updated alpha
        transparent_frames = []
        for frame in self.frames:
            # Create a copy to avoid modifying the original surface
            transparent_frame = frame.copy()
            
            # Set the alpha value for the entire surface
            transparent_frame.set_alpha(alpha)
            
            transparent_frames.append(transparent_frame)
        
        self.frames = transparent_frames
if __name__ == "__main__":
    import sys
    import os
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption("GIF/PNG Loader Test")

    # Test with both GIF and PNG
    gif_path = r"C:\Users\chase\Downloads\R.gif"  # Replace with your GIF path
    png_path = r"C:\Users\chase\OneDrive\Pictures\Screenshots\CHRIS.png"  # Replace with your PNG path
    
    # Create a simple test PNG if it doesn't exist
    if not os.path.exists(png_path):
        test_surface = pygame.Surface((100, 100))
        test_surface.fill((255, 0, 0))
        pygame.image.save(test_surface, png_path)
    
    try:
        gif = GIF(gif_path, scale=1.0, flip_x=True)
        print(f"Loaded GIF: {len(gif.frames)} frames, animated: {gif.is_animated}")
    except Exception as e:
        print(f"Could not load GIF: {e}")
        gif = None
    
    try:
        png = GIF(png_path, scale=0.5)
        print(f"Loaded PNG: {len(png.frames)} frames, animated: {png.is_animated}")
    except Exception as e:
        print(f"Could not load PNG: {e}")
        png = None

    running = True
    while running:
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gif:
                    gif.reset_index()
                if png:
                    png.reset_index()
            
        # Update animations
        if gif:
            gif.update(dt)
        if png:
            png.update(dt)  # This won't do anything for PNG since it's not animated

        # Draw
        screen.fill((30, 30, 30))
        
        # Draw GIF if available
        if gif:
            gif_frame = gif.get_frame()
            if gif_frame:
                rect = gif_frame.get_rect(center=(200, 300))
                screen.blit(gif_frame, rect)
                
                # Display animation status
                font = pygame.font.Font(None, 36)
                status = f"GIF: Frame {gif.current_frame}/{len(gif.frames)}"
                if gif.reached_last_frame():
                    status += " (ENDED)"
                text = font.render(status, True, (255, 255, 255))
                screen.blit(text, (50, 500))
        
        # Draw PNG if available
        if png:
            png_frame = png.get_frame()
            if png_frame:
                rect = png_frame.get_rect(center=(600, 300))
                screen.blit(png_frame, rect)
                
                # Display static image status
                font = pygame.font.Font(None, 36)
                status = "PNG: Static Image"
                text = font.render(status, True, (255, 255, 255))
                screen.blit(text, (450, 500))

        pygame.display.flip()

    pygame.quit()
    sys.exit()