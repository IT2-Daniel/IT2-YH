from panda3d.core import loadPrcFileData

loadPrcFileData('', 'gltf-legacy-materials true')

from ursina import *

app = Ursina()

cube = Entity(
    model="test.glb",
    color=color.red,
    position=(0, 0, 0)
)

EditorCamera()

app.run()