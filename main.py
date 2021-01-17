from mcapi import *
from org.bukkit.event.entity import PlayerDeathEvent
from org.bukkit.event.player import PlayerRespawnEvent


nivel_fl = 0
    
@asynchronous()
def onKill(e):
    global nivel_fl
    jugador = e.getEntity()
    nivel = jugador.getLevel()
    nivel_fl = int(nivel)
    
    nivel_bien = str(nivel)
    yell(nivel_bien)
    return nivel_fl

@asynchronous()
def respawn(e):
    global nivel_fl
    jugadorn = e.getPlayer()
    
    jugadorn.setLevel(nivel_fl)
    yell("respawn")
    


listener = add_event_listener(PlayerDeathEvent, onKill)
listener = add_event_listener(PlayerRespawnEvent, respawn)

