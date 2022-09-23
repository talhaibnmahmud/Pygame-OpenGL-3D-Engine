from source.engine import Engine
from source.model import Cube

if __name__ == "__main__":
    engine = Engine(gl_version=(4, 6))
    engine.set_scene(Cube(engine))
    engine.run()
