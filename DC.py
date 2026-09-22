from ursina import *

app=Ursina()

ground=Entity(model="cube",
              color=color.brown,
              scale=(2000,0,2000),
              y=-1
)
             

player=Entity(model="cube",color=color.azure,scale_y=2,
              position=(0,0,0))

#camera
camera.position=(0,3,-8)
camera.look_at(player)


camera_distance=15
camera_height=5
mouse_sens=40

camera_pivot=Entity(parent=player)
camera_pivot.position=(0,2,0)
camera.parent=camera_pivot
camera.position=(0,camera_height,-camera_distance)

mouse.locked=True


#physics 




gravity=20
vel_y=0
def update():

    #cam rotation
    camera_pivot.rotation_y+=mouse.velocity[0]*mouse_sens
    camera_pivot.rotation_x+=mouse.velocity[1]*mouse_sens

    camera_pivot.rotation_x=clamp(
        camera_pivot.rotation_x,
        -80,
        80
    )

    player_bottom=player.y-player.scale_y/2
    ground_top=ground.y+ground.scale_y/2


    global vel_y
    vel_y-=gravity*time.dt
    player.y+=vel_y*time.dt

    if player_bottom<ground_top:
        player.y=ground_top+player  .scale_y/2
        vel_y=0

    #Player controls


    speed=5*time.dt
    if held_keys["w"]:
        player.z+=speed
    if held_keys["s"]:
        player.z-=speed
    if held_keys["a"]:
        player.x-=speed
    if held_keys["d"]:
        player.x+=speed
  



def input(key):
        global vel_y

        if key == 'space':
            player_bottom=player.y-player.scale_y/2
            ground_top=ground.y+ground.scale_y/2
            if player_bottom==ground_top:
                vel_y = 8

        
app.run()

