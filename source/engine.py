import json
import moderngl
import pygame

from .model import Cube


class Engine:
    def __init__(self, window_size: tuple[int, int] = (800, 600), window_title: str = "ModernGL", gl_version: tuple[int, int] = (3, 3)):
        self.WINDOW_SIZE = window_size
        self.window_title = window_title
        self.gl_version = gl_version

        self.window = None

        # Initialize pygame
        pygame.init()
        pygame.display.set_caption(self.window_title)

        # Set OpenGL Attributes
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_MAJOR_VERSION, self.gl_version[0])
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_MINOR_VERSION, self.gl_version[1])
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        # Create OpenGL Context
        self.window = pygame.display.set_mode(
            self.WINDOW_SIZE, pygame.OPENGL | pygame.DOUBLEBUF
        )

        # Create ModernGL Context
        self.ctx = moderngl.create_context()

        # Create a clock to limit the framerate
        self.clock = pygame.time.Clock()

        # Scene
        # self.scene = Triangle(self.ctx)
        self.scene = Cube(self.ctx)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.scene.destroy()
                pygame.quit()
                exit()

    def render(self):
        # Clear the framebuffer
        self.ctx.clear(0.08, 0.16, 0.16)

        # Render the scene
        self.scene.render()

        # Swap the buffers
        pygame.display.flip()

    def run(self):
        # Print OpenGL Version
        print(json.dumps(self.ctx.info, indent=2))

        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)
