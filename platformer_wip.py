import pygame as pg
import random as r

#setup
pg.init()
screen=pg.display.set_mode((1280,720))
clock=pg.time.Clock()
running=True
dt=0
gravity=1000
vel_y=0
position=pg.Vector2(100, 500)
player=pg.Rect(position.x ,position.y,80,80)
camera_x=player.x
movingPlatform1=pg.Rect(1100, 400, 250, 50)
platform_speed=200
platform_dir=1
hp=3
max_hp=3
enemy_speed=150
enemy_dir=1
enemy_range=300
IFrames=0
spawnX=100
spawnY=500
enemy_hp=2
bullet_speed=500
boss_shottimer=0
boss_shotdelay=0.5
bullet_dir=1
bullet=pg.Rect(player.centerx,player.centery,50,15)
shooting=False
bullet_StartX=0
bullet_range=1000
Boss_hp=15
boss=pg.Rect(4700,100,100,500)
Jump_power=-550
won=False
font = pg.font.Font(None, 50)
bs_cd=0
phase=1
bs_warn=0
bs_shootcd = 0
bs_shootdelay = 0.1
bs_shots = 20
bs_shotsfired = 0







bsl=[
pg.Rect(4000,400,25,100),
pg.Rect(4000,250,25,100),
pg.Rect(4400,600,110,25),
pg.Rect(4225,600,110,25),
pg.Rect(4050,600,110,25)

]

randombs = r.sample(bsl, 2)

randombs=[]


bs_warnt=2
bs_coold=3
bs_atk=False 


boss_bullets=[]
for i in range(15):
    boss_bullets.append(pg.Rect(0,1000,50,15))
    # pg.Rect(boss.x,boss.y,50,15),
    #pg.Rect(boss.x,boss.y,50,15),
    #pg.Rect(boss.x,boss.y,50,15),
    #pg.Rect(boss.x,boss.y,50,15),
    #pg.Rect(boss.x,boss.y,50,15),
    #pg.Rect(boss.x,boss.y,50,15)

bs_bullets=[]
bs_bullet_vel=[]
for i in range(100):
    bs_bullets.append(pg.Rect(0,2000,15,15))
    bs_bullet_vel.append(pg.Vector2(0,0))





platforms = [
    pg.Rect(100, 600, 500, 50),
    pg.Rect(700, 500, 250, 50),
    pg.Rect(1500, 150, 300, 50),
    pg.Rect(2000, 450, 400, 50),
    pg.Rect(2500, 350, 300, 50),
    pg.Rect(3000, 500, 500, 50),
    pg.Rect(3700, 350, 300, 50),
    pg.Rect(4000, 500, 500, 50),

    
]

enemies=[
    {"pos":pg.Vector2(825,450),"rect":pg.Rect(0,0,40,40), "start":825,"dir":1,"hp":2},
    {"pos":pg.Vector2(2200,400),"rect":pg.Rect(0,0,40,40), "start":2200,"dir":1,"hp":2},
    {"pos":pg.Vector2(3250,450),"rect":pg.Rect(0,0,40,40),"start":3250,"dir":1,"hp":2}
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
        vel_y=Jump_power
    if keys[pg.K_s] and vel_y!=0:
         vel_y=500

    if keys[pg.K_a] and keys[pg.K_LSHIFT]:
            player.x-=350*dt
    if keys[pg.K_d] and keys[pg.K_LSHIFT]:
            player.x+=350*dt

    if keys[pg.K_r]:
         hp=0

    

    if keys[pg.K_e] and not shooting:
        shooting = True
        bullet.x = player.right
        bullet.y = player.centery
        bullet_startX = player.right

    if shooting:
        bullet.x += bullet_speed * dt * bullet_dir

        if bullet.x >= bullet_startX + bullet_range:
            shooting = False
            bullet.y = 1000

        screen_bullet = bullet.move(-camera_x, 0)
        pg.draw.rect(screen, "blue", screen_bullet)

    # boss bullets
    for boss_bullet in boss_bullets:
        if boss_bullet.y < 1000:
            screen_boss_bullet = boss_bullet.move(-camera_x, 0)
            pg.draw.rect(screen, "red", screen_boss_bullet)


    #movement
    movingPlatform1.y+=platform_speed*platform_dir*dt

    if movingPlatform1.y>=450:
        platform_dir= -1

    if movingPlatform1.y<=100:
        platform_dir= 1

    boss_shottimer += dt

    if boss_shottimer >= boss_shotdelay and Boss_hp>0:
        boss_shottimer = 0

        for boss_bullet in boss_bullets:
            if boss_bullet.y >= 1000:
                boss_bullet.x = boss.left
                boss_bullet.y = r.randint(boss.top+75, boss.bottom-75 - boss_bullet.height)
                break

    for boss_bullet in boss_bullets:
        if boss_bullet.y < 1000:
            boss_bullet.x -= bullet_speed * dt
            
        if boss_bullet.x < boss.x - 700:
            boss_bullet.y = 1000

 

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
        bullet.y=1000
        print("respawning")
        player.x=spawnX
        player.y=spawnY    
        vel_y=0    
        hp=3
        IFrames=1
        Boss_hp=15
        won=False
        phase=1
        for enemy in enemies:
             enemy["hp"]=2
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
        if enemy["hp"] > 0:

            if enemy["rect"].colliderect(bullet):
                enemy["hp"] -= 1
                bullet.y = 1000
                shooting = False

            if enemy["rect"].colliderect(player) and IFrames <= 0:
                hp -= 1
                IFrames = 1

    for boss_bullet in boss_bullets:
        if boss_bullet.colliderect(player) and IFrames <= 0:
            hp -= 1
            IFrames = 1
            boss_bullet.y = 1000


    # Player HP
    
    for i in range(max_hp):
        if i < hp:
            heart_color = "red"
        else:
            heart_color = "gray"

        pg.draw.circle(screen, heart_color, (40 + i * 45, 40), 15)
        pg.draw.circle(screen, heart_color, (55 + i * 45, 40), 15)
        pg.draw.polygon(screen, heart_color, [
            (25 + i * 45, 45),
            (70 + i * 45, 45),
            (47 + i * 45, 75)
        ])       

      

        # Boss HP bar
    bar_x = 400
    bar_y = 30
    bar_width = 480
    bar_height = 30

    
    pg.draw.rect(screen, "gray", (bar_x, bar_y, bar_width, bar_height))

    
    boss_hp_width = bar_width * Boss_hp / 15

    pg.draw.rect(screen, "red", (
        bar_x,
        bar_y,
        boss_hp_width,
        bar_height
    ))
    if IFrames>0:
         IFrames-=dt


    camera_x=player.centerx-screen.get_width()//2

 #objects
    for platform in platforms:
        screen_platform=platform.move(-camera_x,0)
        pg.draw.rect(screen,"white",screen_platform)

    #for bs in bsl:
        #screen_bs=bs.move(-camera_x,0)
        #pg.draw.rect(screen,"white",screen_bs)
    

    if phase == 2 and Boss_hp>0:
        
        boss_shotdelay=1.25
    
        

        bs_cd += dt

        # Velg to angrepssteder
        if bs_cd >= bs_coold and not bs_atk:
            bs_cd = 0
            randombs = r.sample(bsl, 2)
            bs_warn = 0
            bs_shootcd = 0
            bs_shotsfired = 0
            bs_atk = True

        if bs_atk:

            bs_warn += dt

            # Tegn røde warning-områder
            for bs in randombs:
                screen_bs = bs.move(-camera_x, 0)
                pg.draw.rect(screen, "red", screen_bs)

            # WARNING FERDIG → begynn å skyte
            if bs_warn >= bs_warnt:

                bs_shootcd += dt

                if bs_shootcd >= bs_shootdelay:

                    bs_shootcd = 0

                    for bs in randombs:

                        for i, bs_bullet in enumerate(bs_bullets):

                            # Finn en ledig kule
                            if bs_bullet.y >= 2000:

                                # Skyter oppover
                                if bs.top >= 500:
                                    bs_bullet.x = r.randint(bs.left, bs.right)
                                    bs_bullet.y = bs.top
                                    bs_bullet_vel[i] = pg.Vector2(0, -500)

                                # Skyter mot høyre
                                else:
                                    bs_bullet.x = bs.right
                                    bs_bullet.y = r.randint(bs.top, bs.bottom)
                                    bs_bullet_vel[i] = pg.Vector2(500, 0)

                                bs_shotsfired += 1
                                break

                # Ferdig med å skyte
                if bs_shotsfired >= bs_shots:
                    bs_shotsfired = 0
                    bs_shootcd = 0
                    bs_atk = False
    if phase==1:
        boss_shotdelay=0.5


    # Flytt og tegn aktive Phase-2-kuler
    for i, bs_bullet in enumerate(bs_bullets):

        if bs_bullet.y < 2000:

            bs_bullet.x += bs_bullet_vel[i].x * dt
            bs_bullet.y += bs_bullet_vel[i].y * dt

            screen_bs_bullet = bs_bullet.move(-camera_x, 0)
            pg.draw.rect(screen, "orange", screen_bs_bullet)

            if bs_bullet.colliderect(player) and IFrames<=0:
                hp-=1
                IFrames=1

            # Fjern kule når den har forlatt området
            if bs_bullet.x > 5000 or bs_bullet.y < 0:
                bs_bullet.y = 2000

    screen_movingPlatform1=movingPlatform1.move(-camera_x,0)
    pg.draw.rect(screen,"white", screen_movingPlatform1)

    screen_player=player.move(-camera_x,0)
    if IFrames<=0:
        
        pg.draw.circle(screen, "yellow", screen_player.center,40)
    else:
           pg.draw.circle(screen, "orange", screen_player.center,40)

    for enemy in enemies:
        screen_enemy=enemy["pos"]-pg.Vector2(camera_x,0)
        if enemy["hp"]>0:
            pg.draw.circle(screen,"red",screen_enemy,20)
        else:
             pg.draw.circle(screen,"white",screen_enemy,20) 


    screen_boss=boss.move(-camera_x,0)
    pg.draw.rect(screen,"red",screen_boss)

    if Boss_hp > 0:
    
                if boss.colliderect(bullet):
                    Boss_hp -= 1
                    bullet.y = 1000
                    shooting = False

    if keys[pg.K_n]:
        phase=1
        Boss_hp=15
        hp=3
    if keys[pg.K_m]:
        phase=2
        Boss_hp=15
        hp=5

    if Boss_hp<=0:
         pg.draw.rect(screen,"white",screen_boss)
         if not won:
            max_hp=5
            hp=max_hp
            IFrames=2.5
            Boss_hp=15
    
            for i in range(max_hp):
                if i < hp:
                    heart_color = "red"
                else:
                    heart_color = "gray"
        
                pg.draw.circle(screen, heart_color, (70 + i * 45, 40), 15)
                pg.draw.polygon(screen, heart_color, [
                    (25 + i * 45, 45),
                    (70 + i * 45, 45),
                    (47 + i * 45, 75)
                ])
            phase+=1
            bs_cd=5
            won=True
            print("du vant")
                   
  
    pg.display.flip()
    dt=clock.tick(60)/1000

pg.quit()
