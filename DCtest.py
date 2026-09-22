from ursina import *
from math import *

app = Ursina()

ground = Entity(
    model="cube",
    color=color.brown,
    scale=(2000, 1, 2000),
    y=-1
)

player = Entity(
    model="cube",
    color=color.azure,
    scale_y=2,
    position=(0, 0, 0)
)

# Camera
camera_distance = 15
camera_height = 3
camera_angle_y=0
camera_angle_x=20

mouse_sens = 10





camera.position = (0, camera_height, -camera_distance)

mouse.locked = True


# Physics
gravity = 0
vel_y = 0


def update():
    global vel_y
    global camera_angle_y
    global camera_angle_x

    # -----------------
    # CAMERA position
    # -----------------
    
    camera_angle_y += mouse.velocity[0] * mouse_sens
    camera_angle_x -= mouse.velocity[1] * mouse_sens

    # Stop camera from going upside down
    camera_angle_x = clamp(
        camera_angle_x,
        -80,
        80
    )

    #camera rotation

    
    horizontal_distance=cos(radians(camera_angle_x))*camera_distance
    vertical_distance=sin(radians(camera_angle_x))*camera_distance


    camera.position=player.position+Vec3(
        sin(radians(camera_angle_y))*horizontal_distance,
        camera_height+vertical_distance,
        -cos(radians(camera_angle_y))*horizontal_distance
    )
    
    camera.look_at(player.position+Vec3(0,1,0))
    camera.rotation_z=0



    # -----------------
    # PHYSICS
    # -----------------

    player_bottom = player.y - player.scale_y / 2
    ground_top = ground.y + ground.scale_y / 2

    vel_y -= gravity * time.dt
    player.y += vel_y * time.dt

    if player_bottom < ground_top:
        player.y = ground_top + player.scale_y / 2
        vel_y = 0

    # -----------------
    # PLAYER CONTROLS
    # -----------------

    speed = 5 * time.dt

    if held_keys["w"]:
        player.z += speed

    if held_keys["s"]:
        player.z -= speed

    if held_keys["a"]:
        player.x -= speed

    if held_keys["d"]:
        player.x += speed


def input(key):
    global vel_y

    if key == "space":

        player_bottom = player.y - player.scale_y / 2
        ground_top = ground.y + ground.scale_y / 2

        if player_bottom <= ground_top:
            vel_y = 8

    if key == "escape":
        mouse.locked = not mouse.locked


app.run()