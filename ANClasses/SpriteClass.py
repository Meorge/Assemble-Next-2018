from .BaseClass import *

class NewerCPPClass_Sprite(NewerCPPClass):
    def __init__(self, parent=None):
        super().__init__()
        self.classDisplayName = "Sprite"
        self.classInternalName = "NewerCPPClass_Sprite"
        self.header = """
        #include <common.h>
#include <game.h>
#include <g3dhax.h>
#include <sfx.h>


extern "C" bool SpawnEffect(const char*, int, Vec*, S16Vec*, Vec*);


class ~SPRITETITLE~ : public dEn_c {
        """

        self.collisionFunctions = [
            preSpriteCollision,
            prePlayerCollision,
            preYoshiCollision,
            stageActorCollision,
            spriteCollision,
            playerCollision,
            yoshiCollision,
            collisionCat3_StarPower,
            collisionCat5_Mario,
            _vf108,
            collisionCatD_Drill,
            _vf110,
            collisionCat8_FencePunch,
            collisionCat7_GroundPound,
            collisionCat7_GroundPoundYoshi,
            _vf120,
            collisionCatA_PenguinMario,
            collisionCat11_PipeCannon,
            collisionCat9_RollingObject,
            collisionCat1_Fireball_E_Explosion,
            collisionCat2_IceBall_15_YoshiIce,
            collisionCat13_Hammer,
            collisionCat14_YoshiFire
        ]
        self.functions = [{
        "categoryName": "Collision",
        "categoryFuncs":self.collisionFunctions
        },
        {"categoryName": "Category #2",
        "categoryFuncs": []}
        ]

class CollisionFunc(NewerCPPFunction):
    def __init__(self, parent=None):
        super().__init__()
        self.header = "void ~SPRITETITLE~::~COLLNAME~(ActivePhysics *apThis, ActivePhysics *apOther) {\n"
        self.footer = "}"
        self.validTransformArgs = [
        {
            "argVisibleName": "this actor",
            "argCodeValue": "this",

        },
        {
            "argVisibleName": "colliding actor",
            "argCodeValue": "apOther->owner"
        }]

        



#########################
## Collision functions ##
#########################

class preSpriteCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Before sprite collision"
        self.header = self.header.replace("~COLLNAME~", "preSpriteCollision")

class prePlayerCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Before player collision"
        self.header = self.header.replace("~COLLNAME~", "prePlayerCollision")
        

class preYoshiCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Before Yoshi collision"
        self.header = self.header.replace("~COLLNAME~", "preYoshiCollision")
        

###################
###################

class stageActorCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with an actor"
        self.header = self.header.replace("~COLLNAME~", "stageActorCollision")

###################
###################

class spriteCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with a sprite"
        self.header = self.header.replace("~COLLNAME~", "spriteCollision")

class playerCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with player"
        self.header = self.header.replace("~COLLNAME~", "playerCollision")

class yoshiCollision(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with Yoshi"
        self.header = self.header.replace("~COLLNAME~", "yoshiCollision")

###################
###################

class collisionCat3_StarPower(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with Star Power"
        self.header = self.header.replace("~COLLNAME~", "collisionCat3_StarPower")

class collisionCat5_Mario(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with a player"
        self.header = self.header.replace("~COLLNAME~", "collisionCat3_Mario")

class _vf108(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Unknown (\"_vf108\")"
        self.header = self.header.replace("~COLLNAME~", "_vf108")

class collisionCatD_Drill(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Collided with a drill"
        self.header = self.header.replace("~COLLNAME~", "collisionCatD_Drill")

class _vf110(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Unknown (\"_vf110\")"
        self.header = self.header.replace("~COLLNAME~", "_vf110")

class collisionCat8_FencePunch(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Punched through a fence"
        self.header = self.header.replace("~COLLNAME~", "collisionCat8_FencePunch")

class collisionCat7_GroundPound(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Ground-pounded"
        self.header = self.header.replace("~COLLNAME~", "collisionCat7_GroundPound")

class collisionCat7_GroundPoundYoshi(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Ground-pounded by a Yoshi"
        self.header = self.header.replace("~COLLNAME~", "collisionCat7_GroundPoundYoshi")

class _vf120(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Unknown (\"_vf120\")"
        self.header = self.header.replace("~COLLNAME~", "_vf120")

class collisionCatA_PenguinMario(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a sliding Penguin character"
        self.header = self.header.replace("~COLLNAME~", "collisionCatA_PenguinMario")

class collisionCat11_PipeCannon(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a character out of a pipe cannon"
        self.header = self.header.replace("~COLLNAME~", "collisionCat11_PipeCannon")

class collisionCat9_RollingObject(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a rolling object"
        self.header = self.header.replace("~COLLNAME~", "collisionCat11_RollingObject")

class collisionCat1_Fireball_E_Explosion(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a fireball"
        self.header = self.header.replace("~COLLNAME~", "collisionCat1_Fireball_E_Explosion")

class collisionCat2_IceBall_15_YoshiIce(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by an iceball"
        self.header = self.header.replace("~COLLNAME~", "collisionCat2_IceBall_15_YoshiIce")

class collisionCat13_Hammer(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a hammer"
        self.header = self.header.replace("~COLLNAME~", "collisionCat13_Hammer")

class collisionCat14_YoshiFire(CollisionFunc):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Hit by a Yoshi fireball"
        self.header = self.header.replace("~COLLNAME~", "collisionCat14_YoshiFire")