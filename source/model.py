import glm
import numpy as np


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
        self.update()
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

        return np.array([
            vertices[i] for triangle in indices for i in triangle  # flatten
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
