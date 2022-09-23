import glm
import numpy as np
import pygame


from source.engine import Engine


class Triangle:
    def __init__(self, app: Engine):
        self.app = app
        self.ctx = self.app.ctx
        self.camera = self.app.camera
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program(
            "default.vert", "default.frag"
        )
        self.vao = self.get_vao()

        self.shader_program['projection_matrix'].write(
            self.camera.projection_matrix
        )
        self.shader_program['view_matrix'].write(
            self.camera.view_matrix
        )

        self.model_matrix = self.get_model_matrix()
        self.shader_program['model_matrix'].write(
            self.model_matrix
        )

    def get_model_matrix(self):
        return glm.mat4()

    def update(self):
        model_matrix = glm.rotate(
            self.model_matrix, self.app.time, glm.vec3(0.0, 1.0, 0.0)
        )
        self.shader_program['model_matrix'].write(model_matrix)

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        return self.ctx.vertex_array(
            self.shader_program,
            [(self.vbo, '3f', 'in_position')],
        )

    def get_vertex_data(self):
        return np.array([
            0.0, 0.5, 0.0,
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
        ], dtype='f4')

    def get_vbo(self):
        return self.ctx.buffer(self.get_vertex_data())

    def get_shader_program(self, vertex_shader: str, fragment_shader: str):
        with open(f"source/shaders/{vertex_shader}") as f:
            vertex_code = f.read()

        with open(f"source/shaders/{fragment_shader}") as f:
            fragment_code = f.read()

        return self.ctx.program(
            vertex_shader=vertex_code,
            fragment_shader=fragment_code,
        )


class Cube:
    def __init__(self, app: Engine):
        self.app = app
        self.ctx = self.app.ctx
        self.camera = self.app.camera
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program(
            "default.vert", "default.frag"
        )
        self.vao = self.get_vao()

        # Load texture
        self.texture = self.get_texture("source/textures/test.png")

        # Set texture
        self.shader_program['texture_0'] = 0
        self.texture.use()

        self.shader_program['projection_matrix'].write(
            self.camera.projection_matrix
        )
        self.shader_program['view_matrix'].write(
            self.camera.view_matrix
        )

        self.model_matrix = self.get_model_matrix()
        self.shader_program['model_matrix'].write(
            self.model_matrix
        )

    def get_texture(self, path: str):
        texture = pygame.image.load(path).convert()
        texture = pygame.transform.flip(texture, False, True)
        texture_data = pygame.image.tostring(texture, "RGB")
        return self.ctx.texture(texture.get_size(), 3, texture_data)

    def get_model_matrix(self):
        return glm.mat4()

    def update(self):
        model_matrix = glm.rotate(
            self.model_matrix, self.app.time * 0.5, glm.vec3(0.0, 1.0, 0.0)
        )
        self.shader_program['model_matrix'].write(model_matrix)

    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        return self.ctx.vertex_array(
            self.shader_program,
            [(self.vbo, '2f 3f', 'in_text_coord_0', 'in_position')],
        )

    def get_vertex_data(self):
        vertices = [
            (1.0, -1.0, -1.0), (1.0, 1.0, -1.0), (-1.0,
                                                  1.0, -1.0), (-1.0, -1.0, -1.0),  # front
            (1.0, -1.0, 1.0), (1.0, 1.0, 1.0), (-1.0, - \
                                                1.0, 1.0), (-1.0, 1.0, 1.0),  # back
        ]

        indices = [
            (0, 1, 2), (0, 2, 3),  # front
            (4, 6, 5), (5, 6, 7),  # back
            (0, 3, 6), (0, 6, 4),  # left
            (1, 5, 2), (5, 7, 2),  # right
            (3, 2, 7), (3, 7, 6),  # top
            (0, 4, 1), (1, 4, 5),  # bottom
        ]

        # Texture coordinates
        tex_coords = [(0, 0), (1, 0), (1, 1), (0, 1)]

        # TODO: Fix the indices
        tex_coord_indices = [
            (0, 1, 2), (0, 2, 3),  # front
            (1, 0, 2), (2, 0, 3),  # back
            (0, 1, 2), (0, 2, 3),  # bottom (done)
            (3, 2, 1), (3, 1, 0),  # TODO: top
            (0, 1, 2), (0, 2, 3),  # top
            (1, 0, 2), (2, 0, 3),  # bottom
        ]

        # Texture coordinate data
        tex_coord_data = np.array(
            [tex_coords[i] for j in tex_coord_indices for i in j], dtype='f4'
        )

        vertex_data = np.array([
            vertices[i] for triangle in indices for i in triangle  # flatten
        ], dtype='f4')

        return np.hstack([tex_coord_data, vertex_data])

    def get_vbo(self):
        return self.ctx.buffer(self.get_vertex_data())

    def get_shader_program(self, vertex_shader: str, fragment_shader: str):
        with open(f"source/shaders/{vertex_shader}") as f:
            vertex_code = f.read()

        with open(f"source/shaders/{fragment_shader}") as f:
            fragment_code = f.read()

        return self.ctx.program(
            vertex_shader=vertex_code,
            fragment_shader=fragment_code,
        )
