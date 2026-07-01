@namespace
class SpriteKind:
    money = SpriteKind.create()

def on_overlap_tile(sprite, location):
    level_2()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile)

def on_up_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level 3
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 8))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    global reset
    reset = 1
    game.reset()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, 4))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile7
        """),
    on_overlap_tile4)

def on_on_overlap(sprite5, otherSprite):
    global reset
    reset = 1
    game.reset()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite6, otherSprite2):
    sprites.destroy(mySprite4)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.money, SpriteKind.player, on_on_overlap2)

def on_overlap_tile5(sprite7, location5):
    tiles.set_current_tilemap(tilemap("""
        level 3
        """))
    sprites.destroy(mySprite4)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 8))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
        """),
    on_overlap_tile5)

def level_2():
    global level, mySprite3
    level = 2
    sprites.destroy(mySprite2)
    tiles.set_current_tilemap(tilemap("""
        level0
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 14))
    mySprite3 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    animation.run_image_animation(mySprite3,
        assets.animation("""
            myAnim1
            """),
        2000,
        True)
    tiles.place_on_tile(mySprite3, tiles.get_tile_location(15, 14))

def on_overlap_tile6(sprite8, location6):
    global reset
    reset = 1
    game.reset()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile6)

def on_on_overlap3(sprite9, otherSprite3):
    global reset
    reset = 1
    game.reset()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap3)

def on_overlap_tile7(sprite10, location7):
    global level
    level = 3
    tiles.set_current_tilemap(tilemap("""
        level5
        """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 11))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
        """),
    on_overlap_tile7)

def money_destroy():
    global mySprite4
    mySprite4 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.money)
    animation.run_image_animation(mySprite4,
        assets.animation("""
            myAnim
            """),
        200,
        True)
    tiles.place_on_random_tile(mySprite4, assets.tile("""
        special block meduza
        """))
def strzel():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . 7 7 7 . . . . . . . .
            . . . . . 7 7 7 7 7 7 7 . . . .
            . . . . 7 7 7 7 7 7 7 7 7 7 . .
            . . . 7 7 7 7 7 7 7 7 7 7 7 7 .
            . . 7 7 7 7 7 7 7 7 7 7 7 7 7 .
            . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
            . . 7 7 7 7 7 7 7 7 7 7 7 7 7 .
            . . . 7 7 7 7 7 7 7 7 7 7 . . .
            . . . . . 7 7 7 7 7 7 . . . . .
            """),
        mySprite3,
        -100,
        0)
projectile: Sprite = None
mySprite3: Sprite = None
mySprite4: Sprite = None
mySprite: Sprite = None
mySprite2: Sprite = None
level = 0
reset = 0
money_destroy()
info.set_score(0)
reset = 0
level = 1
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.enemy)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . 3 . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
mySprite.ay = 300
animation.run_image_animation(mySprite, assets.animation("""
    gracz
    """), 200, True)
animation.run_image_animation(mySprite2,
    assets.animation("""
        myAnim0
        """),
    200,
    True)
tiles.set_current_tilemap(tilemap("""
    level
    """))
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile
    """))

def on_on_update():
    controller.move_sprite(mySprite, 100, 0)
    scene.camera_follow_sprite(mySprite)
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(12, 8))
game.on_update(on_on_update)

def on_forever():
    if level == 2:
        pause(2000)
        strzel()
forever(on_forever)
