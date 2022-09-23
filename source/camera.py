import glm
import pygame

from source.engine import Engine

FOV = 45.0
NEAR = 0.1
FAR = 100.0
SPEED = 0.01
SENSITIVITY = 0.05


class Camera:
    def __init__(self, app: Engine, position=(3.0, 3.0, 5.0), yaw=-90.0, pitch=0.0):
        self.app = app
        self.aspect_ratio = app.WINDOW_SIZE[0] / app.WINDOW_SIZE[1]

        # Camera Position
        self.position = glm.vec3(position)

        # Up Vector
        self.up = glm.vec3(0.0, 1.0, 0.0)
        # Forward Vector
        self.forward = glm.vec3(0.0, 0.0, -1.0)
        # Right Vector
        self.right = glm.vec3(1.0, 0.0, 0.0)

        # Yaw and Pitch
        self.yaw = yaw
        self.pitch = pitch

        # View Matrix
        self.view_matrix = glm.lookAt(
            self.position, glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0)
        )

        # Projection Matrix
        self.projection_matrix = self.get_projection_matrix()

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.position += self.forward * velocity
        if keys[pygame.K_s]:
            self.position -= self.forward * velocity
        if keys[pygame.K_a]:
            self.position += self.right * velocity
        if keys[pygame.K_d]:
            self.position -= self.right * velocity
        if keys[pygame.K_q]:
            self.position -= self.up * velocity
        if keys[pygame.K_e]:
            self.position += self.up * velocity

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_rel()
        mouse_x *= SENSITIVITY
        mouse_y *= SENSITIVITY

        self.yaw += mouse_x
        self.pitch += mouse_y

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        # Update camera vectors
        self.forward.x = glm.cos(glm.radians(self.yaw)) * \
            glm.cos(glm.radians(self.pitch))
        self.forward.y = glm.sin(glm.radians(self.pitch))
        self.forward.z = glm.sin(glm.radians(self.yaw)) * \
            glm.cos(glm.radians(self.pitch))
        self.forward = glm.normalize(self.forward)

        self.right = glm.normalize(
            glm.cross(self.forward, glm.vec3(0.0, 1.0, 0.0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()

        self.view_matrix = glm.lookAt(
            self.position, self.position + self.forward, self.up
        )
