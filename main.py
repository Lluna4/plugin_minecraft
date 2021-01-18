from mcapi import *
from org.bukkit.event.entity import PlayerDeathEvent
from org.bukkit.event.player import PlayerRespawnEvent
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player import PlayerVelocityEvent

#beta-dev0.3
def dano_mortal(e):
    entidad = e.getEntity()
    entidad_str = str(entidad)
    
    if entidad_str[:11] == "CraftPlayer":
        vida = float(entidad.getHealth())
        vida_str = str(vida)
        yell(vida_str)
        if vida <= 1.5:
            yell("el poder de los dioses te ha salvado")
            entidad.setHealth(20.0)
        

def revisar_vida(e):
    entidad2 = e.getPlayer()
    
    
    vida2 = float(entidad2.getHealth())
    if vida2 <= 1.5:
        yell("el poder de los dioses te ha salvado")
        entidad2.setHealth(20.0)


listener = add_event_listener(EntityDamageEvent, dano_mortal)
listener2 = add_event_listener(PlayerVelocityEvent, revisar_vida)