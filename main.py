import threading
from mcapi import *
from org.bukkit.event.entity import PlayerDeathEvent
from org.bukkit.event.player import PlayerRespawnEvent
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player import PlayerVelocityEvent

#beta-dev0.5
vida_infinita = False
def se_acabo():
    global vida_infinita
    vida_infinita = False
    return vida_infinita

def dano_mortal(e):
    global vida_infinita
    entidad = e.getEntity()
    entidad_str = str(entidad)
    vida_infinita = False
    if entidad_str[:11] == "CraftPlayer":
        vida = float(entidad.getHealth())
        vida_str = str(vida)
        #yell(vida_str)
        #if e.getDamage() > 0 and vida_infinita == True:
            #entidad.setHealth(20.0)
        if e.getDamage() >= vida:
            yell("REVIVE!!!!!!!!!!!!!!!!")
            entidad.setHealth(20.0)
            lugar = entidad.getLocation()
            entidad.spawnParticle(Particle.SOUL, lugar, 100)
            entidad.playSound(lugar, Sound.BLOCK_ANVIL_LAND, 0.5, 1)
            #vida_infinita = True
            #t = threading.Timer(60, se_acabo)
            #t.start()
    
   

        
        

        



listener = add_event_listener(EntityDamageEvent, dano_mortal)
