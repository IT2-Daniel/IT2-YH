from ursina import *
from math import *

app = Ursina()

ground = Entity(
    model="cube",
    color=color.brown,
    scale=(2000, 1, 2000),
    y=-1,
    collider="box"
)

player = Entity(
    model="cube",
    color=color.azure,
    scale_y=2,
    position=(0, 0, 0),
    collider="box"
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
gravity = 20
vel_y = 0



def ground_collision():
    hit =raycast(
        player.position,
        Vec3(0,-1,0),
        distance=2,
        ignore=[player]
    )


    if hit.hit and vel_y<=0:
        player.y=hit.world_point.y+player.scale_y/2
        return True
    return False

def update():
    global vel_y
    global camera_angle_y
    global camera_angle_x

    on_ground=ground_collision()

    vel_y -= gravity * time.dt
    player.y += vel_y * time.dt

    if on_ground:
        vel_y=0

    if player.y<0:
        player.y=2

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



    # -----------------
    # PLAYER CONTROLS
    # -----------------

    # Movement

    speed=5

    movement = Vec3(
        held_keys["d"] - held_keys["a"],
        0,
        held_keys["w"] - held_keys["s"]
    )

    if movement.length() > 0:
        movement = movement.normalized()

    player.position += movement * speed * time.dt


    # -----------------
    # JUMP
    # -----------------

def input(key):

    global vel_y

    if key == "space" and ground_collision():
        vel_y = 80

    if key == "escape":
        mouse.locked = not mouse.locked


app.run()