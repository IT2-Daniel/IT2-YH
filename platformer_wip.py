import pygame as pg

#setup
pg.init()
screen=pg.display.set_mode((1280,720))
clock=pg.time.Clock()
running=True
dt=0
gravity=1000
vel_y=0
position=pg.Vector2(screen.get_width()/2, screen.get_height()/2)
player=pg.Rect(position.x ,position.y,80,80)
camera_x=player.x
movingPlatform1=pg.Rect(1100, 400, 250, 50)
platform_speed=200
platform_dir=1
hp=3
enemy_speed=150
enemy_dir=1
enemy_range=300
IFrames=0
spawnX=100
spawnY=500


platforms = [
    pg.Rect(100, 600, 500, 50),
    pg.Rect(700, 500, 250, 50),
    pg.Rect(1500, 150, 300, 50),
    pg.Rect(2000, 450, 400, 50),
    pg.Rect(2500, 350, 300, 50),
    pg.Rect(3000, 500, 500, 50),
    
]

enemies=[
    {"pos":pg.Vector2(825,400),"rect":pg.Rect(0,0,80,80), "start":825,"dir":1},
    {"pos":pg.Vector2(2200,350),"rect":pg.Rect(0,0,80,80), "start":2200,"dir":1},
    {"pos":pg.Vector2(3250,400),"rect":pg.Rect(0,0,80,80),"start":3250,"dir":1}
]


while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

    screen.fill("purple")

    #controls
    keys=pg.key.get_pressed()
    if keys[pg.K_a]:
        player.x-=300*dt
    if keys[pg.K_d]:
        player.x+=300*dt
    if keys[pg.K_SPACE] and vel_y==0:
        vel_y=-500

    if keys[pg.K_a] and keys[pg.K_LSHIFT]:
            player.x-=350*dt
    if keys[pg.K_d] and keys[pg.K_LSHIFT]:
            player.x+=350*dt


    #movement
    movingPlatform1.y+=platform_speed*platform_dir*dt

    if movingPlatform1.y>=450:
        platform_dir= -1

    if movingPlatform1.y<=100:
        platform_dir= 1

 

    for enemy in enemies:
        enemy["pos"].x+=enemy_speed*enemy["dir"]*dt

        if enemy["pos"].x>=enemy["start"]+enemy_range:
            enemy["dir"]=-1 

        if enemy["pos"].x<=enemy["start"]-enemy_range:
                    enemy["dir"]=1 

        enemy["rect"].center=enemy["pos"]

     #physics

    
    old_bottom=player.bottom

    vel_y+=gravity*dt
    player.y+=vel_y*dt



  


    player.y = max(0, min(player.y, 720-player.height))

    if player.bottom>=720:
        hp=0

    if hp<=0:
        print("respawning")
        player.x=spawnX
        player.y=spawnY    
        vel_y=0    
        hp=3
        IFrames=1
        continue 

    for platform in platforms:
        if player.colliderect(platform):
         if vel_y>0 and old_bottom<=platform.top:
            player.bottom=platform.top
            vel_y=0

    if player.colliderect(movingPlatform1):
        if vel_y > 0:
            player.bottom = movingPlatform1.top
            vel_y = 0

    for enemy in enemies:
         if enemy["rect"].colliderect(player) and IFrames<=0:
              hp-=1
              IFrames=1

    if IFrames>0:
         IFrames-=dt


    camera_x=player.centerx-screen.get_width()//2

 #objects
    for platform in platforms:
        screen_platform=platform.move(-camera_x,0)
        pg.draw.rect(screen,"white",screen_platform)

    screen_movingPlatform1=movingPlatform1.move(-camera_x,0)
    pg.draw.rect(screen,"white", screen_movingPlatform1)
    
    screen_player=player.move(-camera_x,0)
    if IFrames<=0:
        
        pg.draw.circle(screen, "yellow", screen_player.center,40)
    else:
           pg.draw.circle(screen, "orange", screen_player.center,40)

    for enemy in enemies:
        screen_enemy=enemy["pos"]-pg.Vector2(camera_x,0)
        pg.draw.circle(screen,"red",screen_enemy,40)

  
    pg.display.flip()
    dt=clock.tick(60)/1000

pg.quit()
