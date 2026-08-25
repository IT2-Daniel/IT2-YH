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
platform1=pg.Rect(1000,500,250,50)
platform2=pg.Rect(100,500,250,50)
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

    screen.fill("purple")

 

    pg.draw.rect(screen, "white",platform1)
    pg.draw.rect(screen, "white",platform2)

    pg.draw.circle(screen, "yellow", player.center,40)
    keys=pg.key.get_pressed()
    if keys[pg.K_w]:
        player.y-=300*dt
    if keys[pg.K_s]:
        player.y+=300*dt
    if keys[pg.K_a]:
        player.x-=300*dt
    if keys[pg.K_d]:
        player.x+=300*dt
    if keys[pg.K_SPACE]:
        vel_y=-500



    vel_y+=gravity*dt
    player.y+=vel_y*dt

    player.x = max(0, min(player.x, 1280-player.width))
    player.y = max(0, min(player.y, 720-player.height))

    if player.bottom>=720:
        player.bottom=720
        vel_y=0


    if player.colliderect(platform1):
        if vel_y>0:
            player.bottom=platform1.top
            vel_y=0

    if player.colliderect(platform2):
            if vel_y>0:
                player.bottom=platform2.top
                vel_y=0

    pg.display.flip()
    dt=clock.tick(60)/1000

pg.quit()
