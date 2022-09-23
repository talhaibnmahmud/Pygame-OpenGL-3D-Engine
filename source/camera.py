import glm

FOV = 45.0
NEAR = 0.1
FAR = 100.0


class Camera:
    def __init__(self, window_size: tuple[int, int]):
        self.aspect_ratio = window_size[0] / window_size[1]

        # Camera Position
        self.position = glm.vec3(3.0, 3.0, 5.0)
        # Up Vector
        self.up = glm.vec3(0.0, 1.0, 0.0)

        # View Matrix
        self.view_matrix = glm.lookAt(
            self.position, glm.vec3(0.0, 0.0, 0.0), self.up
        )

        # Projection Matrix
        self.projection_matrix = self.get_projection_matrix()

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
