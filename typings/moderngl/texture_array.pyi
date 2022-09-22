"""
This type stub file was generated by pyright.
"""

from typing import Tuple

__all__ = ['TextureArray']
class TextureArray:
    '''
        An Array Texture is a Texture where each mipmap level contains an array of
        images of the same size. Array textures may have Mipmaps, but each mipmap
        in the texture has the same number of levels.

        A TextureArray object cannot be instantiated directly, it requires a context.
        Use :py:meth:`Context.texture_array` to create one.
    '''
    __slots__ = ...
    def __init__(self) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @property
    def repeat_x(self) -> bool:
        '''
            bool: The x repeat flag for the texture (Default ``True``)

            Example::

                # Enable texture repeat (GL_REPEAT)
                texture.repeat_x = True

                # Disable texture repeat (GL_CLAMP_TO_EDGE)
                texture.repeat_x = False
        '''
        ...
    
    @repeat_x.setter
    def repeat_x(self, value): # -> None:
        ...
    
    @property
    def repeat_y(self) -> bool:
        '''
            bool: The y repeat flag for the texture (Default ``True``)

            Example::

                # Enable texture repeat (GL_REPEAT)
                texture.repeat_y = True

                # Disable texture repeat (GL_CLAMP_TO_EDGE)
                texture.repeat_y = False
        '''
        ...
    
    @repeat_y.setter
    def repeat_y(self, value): # -> None:
        ...
    
    @property
    def filter(self) -> Tuple[int, int]:
        '''
            tuple: The minification and magnification filter for the texture.
            (Default ``(moderngl.LINEAR. moderngl.LINEAR)``)

            Example::

                texture.filter == (moderngl.NEAREST, moderngl.NEAREST)
                texture.filter == (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
                texture.filter == (moderngl.NEAREST_MIPMAP_LINEAR, moderngl.NEAREST)
                texture.filter == (moderngl.LINEAR_MIPMAP_NEAREST, moderngl.NEAREST)
        '''
        ...
    
    @filter.setter
    def filter(self, value): # -> None:
        ...
    
    @property
    def swizzle(self) -> str:
        '''
            str: The swizzle mask of the texture (Default ``'RGBA'``).

            The swizzle mask change/reorder the ``vec4`` value returned by the ``texture()`` function
            in a GLSL shaders. This is represented by a 4 character string were each
            character can be::

                'R' GL_RED
                'G' GL_GREEN
                'B' GL_BLUE
                'A' GL_ALPHA
                '0' GL_ZERO
                '1' GL_ONE

            Example::

                # Alpha channel will always return 1.0
                texture.swizzle = 'RGB1'

                # Only return the red component. The rest is masked to 0.0
                texture.swizzle = 'R000'

                # Reverse the components
                texture.swizzle = 'ABGR'
        '''
        ...
    
    @swizzle.setter
    def swizzle(self, value): # -> None:
        ...
    
    @property
    def anisotropy(self) -> float:
        '''
            float: Number of samples for anisotropic filtering (Default ``1.0``).
            The value will be clamped in range ``1.0`` and ``ctx.max_anisotropy``.

            Any value greater than 1.0 counts as a use of anisotropic filtering::

                # Disable anisotropic filtering
                texture.anisotropy = 1.0

                # Enable anisotropic filtering suggesting 16 samples as a maximum
                texture.anisotropy = 16.0
        '''
        ...
    
    @anisotropy.setter
    def anisotropy(self, value): # -> None:
        ...
    
    @property
    def width(self) -> int:
        '''
            int: The width of the texture array.
        '''
        ...
    
    @property
    def height(self) -> int:
        '''
            int: The height of the texture array.
        '''
        ...
    
    @property
    def layers(self) -> int:
        '''
            int: The number of layers of the texture array.
        '''
        ...
    
    @property
    def size(self) -> tuple:
        '''
            tuple: The size of the texture array.
        '''
        ...
    
    @property
    def components(self) -> int:
        '''
            int: The number of components of the texture array.
        '''
        ...
    
    @property
    def dtype(self) -> str:
        '''
            str: Data type.
        '''
        ...
    
    @property
    def glo(self) -> int:
        '''
            int: The internal OpenGL object.
            This values is provided for debug purposes only.
        '''
        ...
    
    def read(self, *, alignment=...) -> bytes:
        '''
            Read the pixel data as bytes into system memory.

            Keyword Args:
                alignment (int): The byte alignment of the pixels.

            Returns:
                bytes
        '''
        ...
    
    def read_into(self, buffer, *, alignment=..., write_offset=...) -> None:
        '''
            Read the content of the texture array into a bytearray or :py:class:`~moderngl.Buffer`.
            The advantage of reading into a :py:class:`~moderngl.Buffer` is that pixel data
            does not need to travel all the way to system memory::

                # Reading pixel data into a bytearray
                data = bytearray(8)
                texture = ctx.texture((2, 2, 2), 1)
                texture.read_into(data)

                # Reading pixel data into a buffer
                data = ctx.buffer(reserve=8)
                texture = ctx.texture((2, 2, 2), 1)
                texture.read_into(data)

            Args:
                buffer (Union[bytearray, Buffer]): The buffer that will receive the pixels.

            Keyword Args:
                alignment (int): The byte alignment of the pixels.
                write_offset (int): The write offset.
        '''
        ...
    
    def write(self, data, viewport=..., *, alignment=...) -> None:
        '''
            Update the content of the texture array from byte data
            or a moderngl :py:class:`~moderngl.Buffer`.

            The ``viewport`` can be used for finer control of where the
            data should be written in the array. The valid versions are::

                # Writing multiple layers from the begining of the texture
                texture.write(data, viewport=(width, hight, num_layers))

                # Writing sub-sections of the array
                texture.write(data, viewport=(x, y, layer, width, height, num_layers))

            Like with other texture types we can also use bytes or :py:class:`~moderngl.Buffer`
            as a source::

                # Using a moderngl buffer
                data = ctx.buffer(reserve=8)
                texture = ctx.texture_array((2, 2, 2), 1)
                texture.write(data)

                # Using byte data from system memory
                data = b"\xff\xff\xff\xff\xff\xff\xff\xff"
                texture = ctx.texture_array((2, 2, 2), 1)
                texture.write(data)

            Args:
                data (bytes): The pixel data.
                viewport (tuple): The viewport.

            Keyword Args:
                alignment (int): The byte alignment of the pixels.
        '''
        ...
    
    def build_mipmaps(self, base=..., max_level=...) -> None:
        '''
            Generate mipmaps.

            This also changes the texture filter to ``LINEAR_MIPMAP_LINEAR, LINEAR``
            (Will be removed in ``6.x``)

            Keyword Args:
                base (int): The base level
                max_level (int): The maximum levels to generate
        '''
        ...
    
    def use(self, location=...) -> None:
        '''
            Bind the texture to a texture unit.

            The location is the texture unit we want to bind the texture.
            This should correspond with the value of the ``sampler2DArray``
            uniform in the shader because samplers read from the texture
            unit we assign to them::

                # Define what texture unit our two sampler2DArray uniforms should represent
                program['texture_a'] = 0
                program['texture_b'] = 1
                # Bind textures to the texture units
                first_texture.use(location=0)
                second_texture.use(location=1)

            Args:
                location (int): The texture location/unit.
        '''
        ...
    
    def release(self) -> None:
        '''
            Release the ModernGL object.
        '''
        ...
    


