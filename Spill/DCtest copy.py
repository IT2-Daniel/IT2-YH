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





#player = Entity(
  #  model="cube",
  #  color=color.azure,
  #  scale_y=2,
   # position=(0, 0, 0),
   # collider="box"
#)



test=Entity(
    model="cube",
    color=color.orange,
    scale=(10,10,10),
    position=(20,0,20)
)

class Player:
    def __init__(self,x,y,z):
        self.entity=Entity(
            model="Emilplayer.glb",
            position=(x, y, z),
            scale=0.2,
            collider="box"
        )

        self.gravity=20
        self.vel_y=0
        self.speed=5

    def ground_collision(self):
        hit=raycast(
            self.entity.position,
            Vec3(0,-1,0),
            distance=2,
            ignore=[self.entity]
    
        )

        if hit.hit and self.vel_y<=0:
            self.entity.y=hit.world_point.y+self.entity.scale_y/2
            return True

        return False

    def move(self):
        speed=self.speed

        if held_keys["shift"]:
            speed=20

        forward=Vec3(camera.forward.x,0,camera.forward.z).normalized()
        right=Vec3(camera.right.x,0,camera.right.z).normalized()



        movement=(
            forward*(held_keys["w"]-held_keys["s"])
            +right*(held_keys["d"]-held_keys["a"])
        )

        if movement.length()>0:
            movement=movement.normalized()

        self.entity.position+=movement*speed*time.dt

    def update(self):
        on_ground=self.ground_collision()

        if on_ground and self.vel_y<0:
            self.vel_y=0

        self.vel_y-=self.gravity*time.dt
        self.entity.y+=self.vel_y*time.dt

        self.move()

    def jump(self):
        if self.ground_collision():
            self.vel_y=8


class Enemy_war:
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
        self.entity.x+=self.speed*time.dt


player1 = Player(0,50,0)

def update():
    player1.update()

def input(key):
    if key=="space":
        player1.jump()


enemies=[
Enemy_war(0,-6.6414,10),
Enemy_war(10,-6.6414,10),
Enemy_war(20,-6.6414,10)

]




# Camera
camera_distance = 15
camera_height = 3
camera_angle_y=0
camera_angle_x=20

mouse_sens = 10




mouse.locked = True








def update():
    global camera_angle_y,camera_angle_x

    player1.update()

    for enemy in enemies:
        enemy.move()
  



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


    camera.position=player1.entity.position+Vec3(
        sin(radians(camera_angle_y))*horizontal_distance,
        camera_height+vertical_distance,
        -cos(radians(camera_angle_y))*horizontal_distance
    )
    
    camera.look_at(player1.entity.position+Vec3(0,1,0))
    camera.rotation_z=0


def input(key):
    if key=="space":
        player1.jump()

    if key=="escape":
        mouse.locked=False


app.run()