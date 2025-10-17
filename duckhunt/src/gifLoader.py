from PIL import Image
import pygame

class GIF:
    def __init__(self, filepath, scale=1.0, flip_x=False, flip_y=False):
        """Load a GIF and extract frames into Pygame surfaces."""
        self.filepath = filepath
        self.frames = []
        self.frame_durations = []

        self.scale = scale
        self.flip_x = flip_x
        self.flip_y = flip_y

        # Load GIF with Pillow
        pil_gif = Image.open(filepath)
        
        try:
            while True:
                frame = pil_gif.convert("RGBA")
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

                duration = pil_gif.info.get('duration', 100)
                self.frame_durations.append(duration)

                pil_gif.seek(pil_gif.tell() + 1)
        except EOFError:
            pass

        self.current_frame = 0
        self.time_accumulator = 0

    def update(self, dt=100):
        """Update frame based on elapsed time (dt in milliseconds)."""
        if not self.frames:
            return

        self.time_accumulator += dt
        if self.current_frame < len(self.frames):
            if self.time_accumulator >= self.frame_durations[self.current_frame]:
                self.time_accumulator = 0
                self.current_frame += 1 # update frame index

    def get_frame(self):
        """Return the current frame surface."""
        if self.frames and self.current_frame<len(self.frames):
            return self.frames[self.current_frame]
        return self.frames[-1] # always return a frame

    def reset_index(self):
        self.current_frame = 0
        self.time_accumulator = 0

    def reached_last_frame(self):
        return self.current_frame>=len(self.frames)
    
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
if __name__ == "__main__":
    import sys
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    gif = GIF(r"C:\Users\chase\Downloads\R.gif", scale=1.0, flip_x=True)

    running = True
    while running:
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gif.reset_index()
            

        gif.update(dt)
        frame = gif.get_frame()

        if frame:
            screen.fill((30, 30, 30))
            rect = frame.get_rect(center=screen.get_rect().center)
            screen.blit(frame, rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
