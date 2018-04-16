from gamelib import * #Imports gamelib. Essential for any game.

game = Game (800, 600, "Treasure Hunters") #

#Graphics
play = Image ("button-start-game.png", game)
play.y += 50
play.resizeBy (-25)

bk = Image ("Background.jpg", game)

cave = Image ("Cave.jpg", game)
cave.resizeTo (800, 600)
game.setBackground (cave)

logo = Image ("Logo.png", game)
logo.resizeBy (-35)
logo.y -= 150

platform = Image ("Platform.png", game)
platform.resizeTo (800, 200)

explorer = Animation("explorer.png", 8, game, 786/4, 472/2)
explorer.resizeBy (-40)
explorer.moveTo (100, 450)

treasure = Image ("treasure.png", game, use_alpha = True)
treasure.moveTo (700, 420)
treasure.resizeTo (200, 200)
treasure.visible = False

congrats = Image("Congrats.png", game)
congrats.moveTo (400, 150)

death = Image ("Death.png", game)
death.resizeTo (800, 600)

deadbody = Image ("DeadExplorer.png", game)
deadbody.moveTo (417, 140)
deadbody.resizeBy (-55)

scroll = Image ("Scroll.jpg", game)
scroll.resizeTo (800, 180)
scroll.moveTo (400, 510)

sunshine = Image ("Sunshine.png", game)
sunshine.visible = False
sunshine.moveTo (treasure.x, treasure.y)
sunshine.resizeBy (-60)

#Hearts
hp = Image ("heart.png",game)
hp.moveTo (590, 50)
hp.resizeBy (-50)

hp2 = Image ("heart.png", game)
hp2.moveTo (675, 50)
hp2.resizeBy (-50)

hp3 = Image ("heart.png", game)
hp3.moveTo (760, 50)
hp3.resizeBy (-50)

#Traps
traps = []
for index in range (30):
    traps.append (Image("Spike.png", game))

x = randint (400, 800)
for index in range (30):
    traps[index].moveTo (1500, 450)
    traps[index].resizeBy (-50)
    traps[index].setSpeed (3, 90)

traps2 = []
for index in range (30):
    traps2.append (Image("Spike.png", game))

x = randint (400, 800)
for index in range (30):
    traps2[index].moveTo (1750, 450)
    traps2[index].resizeBy (-50)
    traps2[index].setSpeed (3, 90)

#Icicles
icicles = []
for index in range(30):
    icicles.append(Image("Ice.png",game))

for index in range (30):
    x = randint (100, 700)
    y = randint (100, 300)
    icicles[index].moveTo (x, -y)
    icicles[index].resizeBy (-75)
    s = randint (3, 6) 
    icicles[index].setSpeed (s, 180)

#Bats
bat = []
for index in range(30):
    bat.append(Animation("bat.png", 8, game, 298/5, 286/5))

for index in range (30):
    x = randint (-75, -50)
    y = randint (100, 500)
    bat[index].moveTo (x, y)
    s = randint (8, 10) 
    bat[index].setSpeed (s, -90)

#Sounds
victory = Sound("exit_cue_y.wav", 1)
music = Sound ("Music.wav", 2)

#Title Screen
game.over = False
game.setMusic ("Music.wav")
game.playMusic ()

while not game.over:
    game.processInput()

    bk.draw ()
    play.draw()
    logo.draw ()
    scroll.draw ()
   
    f = Font(black, 25, white, "Times")
    game.drawText ("@2018, SIK Games Inc", 650, 580)
    game.drawText ("STORY: You are an explorer carrying the legacy of your father,", 100, 435, f)
    game.drawText ("You have found a dark cave and you begin to explore,", 120, 455, f)
    game.drawText("There are many dangerous obstacles along the way, try to avoid them!", 50, 475, f)
    game.drawText ("If you don't, you will take damage.", 200, 495, f)
    game.drawText ("If you take enough damage, you will die.", 165, 515, f)
    game.drawText ("Once you have successfully avoided all the obstacles,", 120, 535, f)
    game.drawText ("You will be greatly rewarded with the treausre.", 130, 555, f)

    if play.collidedWith (mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)

#Game
trapsPassed = 0
Icicles = 0
Bat = 0
game.over = False
while not game.over:
    game.processInput ()
    game.scrollBackground ("left", 3)
    platform.draw ()
    traps[index].move ()
    traps2[index].move ()
    hp.draw ()
    hp2.draw ()
    hp3.draw ()

    if traps[index].collidedWith (explorer, "circle") or traps2[index].collidedWith (explorer, "circle"):
        explorer.health -= 1

    if explorer.health < 70:
        hp.visible = False

    if explorer.health < 50:
        hp2.visible = False

    if explorer.health is 0:
        hp3.visible = False
        
    
    r = randint (800, 1500)

    if traps[index].isOffScreen ("left"):
        traps[index].moveTo(r, 450)
        trapsPassed +=1

    if traps2[index].isOffScreen ("left"):
        traps2[index].moveTo(r, 450)
        trapsPassed +=1

    if trapsPassed >= 15:
        icicles[index].move ()

    if trapsPassed >= 5:
        bat[index].move ()

    x = randint (-75, -50)
    y = randint (100, 500)

    if bat[index].isOffScreen ("right"):
        bat[index].moveTo (x, y)
        batspeed = randint (8, 10)
        bat[index].setSpeed (batspeed, -90)
        Bat +=1

    if bat[index].collidedWith (explorer):
        explorer.health -=5
        bat[index].moveTo(x, y)
        batspeed = randint (8, 10)
        bat[index].setSpeed (batspeed, -90)
        Bat +=1
                           
        
    icex = randint (100, 700)
    icey = randint (100, 300)
    if icicles[index].collidedWith (platform, "rectangle"):
        icicles[index].moveTo(icex, -icey)
        ices = randint (3, 6) 
        icicles[index].setSpeed (ices, 180)
        Icicles +=1

    if icicles[index].collidedWith (explorer):
        explorer.health -=5
        icicles[index].moveTo(icex, -icey)
        ices = randint (3, 6) 
        icicles[index].setSpeed (ices, 180)
        Icicles +=1
   
    if icicles[index].x is 0:
        icicles[index].visible = True
    
    platform.moveTo (400, 600)

#Prevent explorer going off left side of the screen
    if explorer.left <= game.left:
        explorer.x = explorer.width / 2

    if explorer.isOffScreen ("top"):
        game.over = True

    if explorer.isOffScreen ("right"):
        game.over = True


    if trapsPassed >= 30 and Icicles >= 15 and Bat >= 30:
        traps[index].visible = False
        traps2[index].visible = False
        icicles[index].visible = False
        bat[index].visible = False
        treasure.visible = True
        sunshine.visible = True
        sunshine.draw ()
        treasure.draw ()
        game.stopMusic ()
    
        
    if treasure.collidedWith (explorer):
        congrats.draw ()
        victory.play ()
        game.drawText("Press ESC To Exit the Game", 300, 250)

        if keys.Pressed [K_ESCAPE]:
            game.over = True

    onrock = False
    jumping = False
    factor = 1
    landed = False

#Jumping Logic
    if jumping:
        explorer.y -= 18 * factor
        factor *= .95
        landed = False
    if factor < .5:
        jumping = False
        factor = 1
    if keys.Pressed[K_SPACE] and not jumping:
        jumping = True
            
    if not onrock and jumping:
        explorer.y -= 10

    if not jumping:
        explorer.y += 5


    if explorer.bottom > platform.top:
        explorer.y = explorer.y / 1.015

    if keys.Pressed[K_RIGHT]:  
        explorer.prevFrame ()
        explorer.x += 6
    if keys.Pressed[K_LEFT]:
        explorer.prevFrame ()
        explorer.x -= 6


    explorer.draw ()

  
    game.drawText("Health: " + str(explorer.health),hp.x - 20,hp.y + 50)
    game.drawText ("Press Left / Right Arrows to Move Left / Right", 25, 50)
    game.drawText ("Press Spacebar to Jump!", 25, 75)
    game.drawText ("Don't go off the screen or you will die!", 25, 100)
    game.drawText ("@2018, SIK Games Inc", 650, 580)

#Death Screen
    if explorer.health <= 0:
        game.stopMusic ()
        death.draw ()
        deadbody.draw ()
        game.drawText ("Press ESC To Exit the Game", 300, 250)

        if keys.Pressed [K_ESCAPE]:
            game.over = True
            
    game.update (30)
game.quit ()
