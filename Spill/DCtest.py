from ursina import *
from math import *


app = Ursina()

ground = Entity(
    model="cube",
    texture="grass",
    texture_scale=(200,200),
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


test=Entity(
    model="cube",
    color=color.orange,
    scale=(10,10,10),
    position=(20,0,20)
)

class enemy_war:
    def __init__(self,x,y,z):
        self.entity=Entity(
            model="larsmedsverdblend1.glb",
            position=(x,y,z),
            scale=1
            
        )
        self.x=x
        self.y=y
        self.z=z
        self.hp=100
        self.speed=7
        self.damage=10

    def move(self):
        self.x+=self.speed

enemy1=enemy_war(0,-6.414,10)
enemy1.move()

enemy2=enemy_war(10,-6.6414,10)
enemy2.move()

enemy3=enemy_war(20,-6.6414,10)
enemy3.move()


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
    
    camera_angle_y -= mouse.velocity[0] * mouse_sens
    camera_angle_x += mouse.velocity[1] * mouse_sens

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

    if held_keys["shift"]:
        speed=20
    else:
        speed=5


    forward = Vec3(camera.forward.x, 0, camera.forward.z).normalized()
    right = Vec3(camera.right.x, 0, camera.right.z).normalized()

    movement = (
        forward * (held_keys["w"] - held_keys["s"])
        + right * (held_keys["d"] - held_keys["a"])
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
        vel_y = 8

    if key == "escape":
        mouse.locked = not mouse.locked


app.run()