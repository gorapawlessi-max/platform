namespace SpriteKind {
    export const money = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile7`, function (sprite4, location4) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 4))
})
function money_destroy () {
    mySprite4 = sprites.create(img`
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
        `, SpriteKind.money)
    animation.runImageAnimation(
    mySprite4,
    assets.animation`myAnim`,
    200,
    true
    )
    tiles.placeOnRandomTile(mySprite4, assets.tile`special block meduza`)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    level_2()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite10, location7) {
    level = 3
    tiles.setCurrentTilemap(tilemap`level5`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 11))
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -150
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava1, function (sprite8, location6) {
    reset = 1
    game.reset()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite3, location3) {
    reset = 1
    game.reset()
})
function level_2 () {
    level = 2
    sprites.destroy(mySprite2)
    tiles.setCurrentTilemap(tilemap`level0`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 14))
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    mySprite3,
    assets.animation`myAnim1`,
    2000,
    true
    )
    tiles.placeOnTile(mySprite3, tiles.getTileLocation(15, 14))
}
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite9, otherSprite3) {
    reset = 1
    game.reset()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite5, otherSprite) {
    reset = 1
    game.reset()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile9`, function (sprite7, location5) {
    tiles.setCurrentTilemap(tilemap`level 3`)
    sprites.destroy(mySprite4)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 8))
})
function strzel () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite3, -100, 0)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile6`, function (sprite2, location2) {
    tiles.setCurrentTilemap(tilemap`level 3`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 8))
})
sprites.onOverlap(SpriteKind.money, SpriteKind.Player, function (sprite6, otherSprite2) {
    sprites.destroy(mySprite4)
    info.changeScoreBy(1)
})
let projectile: Sprite = null
let mySprite3: Sprite = null
let mySprite4: Sprite = null
let mySprite: Sprite = null
let mySprite2: Sprite = null
let level = 0
let reset = 0
money_destroy()
info.setScore(0)
reset = 0
level = 1
mySprite2 = sprites.create(img`
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
    `, SpriteKind.Enemy)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.ay = 300
animation.runImageAnimation(
mySprite,
assets.animation`gracz`,
200,
true
)
animation.runImageAnimation(
mySprite2,
assets.animation`myAnim0`,
200,
true
)
tiles.setCurrentTilemap(tilemap`level`)
tiles.placeOnRandomTile(mySprite, assets.tile`myTile`)
game.onUpdate(function () {
    controller.moveSprite(mySprite, 100, 0)
    scene.cameraFollowSprite(mySprite)
    tiles.placeOnTile(mySprite2, tiles.getTileLocation(12, 8))
})
forever(function () {
    if (level == 2) {
        pause(2000)
        strzel()
    }
})
