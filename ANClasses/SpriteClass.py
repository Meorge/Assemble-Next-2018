from .BaseClass import *

class NewerCPPClass_Sprite(NewerCPPClass):
    def __init__(self, parent=None):
        self.className = "Sprite"
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
        	collisionCat3_StarPower
        ]
        self.functions = [{
        "categoryName": "Collision",
        "categoryFuncs":self.collisionFunctions
        }]

class CollisionFunc(NewerCPPFunction):
	validTransformArgs = [
	{
	    "argVisibleName": "this actor",
	    "argCodeValue": "this",

	},
	{
	    "argVisibleName": "colliding actor",
	    "argCodeValue": "apOther->owner"
	}]
	def __init__(self, parent=None):
		self.header = "void ~SPRITETITLE~::~COLLNAME~(ActivePhysics *apThis, ActivePhysics *apOther) {\n"
		self.footer = "}"



#########################
## Collision functions ##
#########################

class preSpriteCollision(CollisionFunc):
	def __init__(self, parent=None):
		self.title = "Before sprite collision"
		self.header = self.header.replace("~COLLNAME~", "preSpriteCollision")

class prePlayerCollision(CollisionFunc):
	def __init__(self, parent=None):
		self.title = "Before player collision"
		self.header = self.header.replace("~COLLNAME~", "prePlayerCollision")

class preYoshiCollision(CollisionFunc):
	def __init__(self, parent=None):
		self.title = "Before Yoshi collision"
		self.header = self.header.replace("~COLLNAME~", "preYoshiCollision")

###################
###################

class stageActorCollision(CollisionFunc):
	def __init__(self, parent=None):
		self.title = "Collided with an actor"
		self.header = self.header.replace("~COLLNAME~", "stageActorCollision")

###################
###################

class spriteCollision(CollisionFunc):
	def __init__(self, parent=None):
		self.title = "Collided with a sprite"
		self.header = self.header.replace("~COLLNAME~", "spriteCollision")

class playerCollision(CollisionFunc):
	def __init__(self, parent=None):
	    self.title = "Collided with player"
	    self.header = self.header.replace("~COLLNAME~", "playerCollision")

class yoshiCollision(CollisionFunc):
	def __init__(self, parent=None):
	    self.title = "Collided with Yoshi"
	    self.header = self.header.replace("~COLLNAME~", "yoshiCollision")

###################
###################

class collisionCat3_StarPower(CollisionFunc):
	def __init__(self, parent=None):
	    self.title = "Collided with Star Power"
	    self.header = self.header.replace("~COLLNAME~", "collisionCat3_StarPower")