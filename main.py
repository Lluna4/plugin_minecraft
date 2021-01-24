import threading
import datetime
from mcapi import *
from org.bukkit.event.entity import PlayerDeathEvent
from org.bukkit.event.player import PlayerRespawnEvent
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player import PlayerVelocityEvent

#beta-dev0.6
def conexion(e):
    jugador = e.getPlayer()
    jugador_str = str(jugador)
    jugador_str2 = jugador_str + "!"
    try:
        with open(jugador_str, "r") as j_r:
            dia = j_r.read()
            dia_ahora = datetime.datetime.now()
            if dia_ahora.day - dia > 0:
                with open(jugador_str, "w") as j_w:
                    j_w.write(dia_ahora.day)
                with open(jugador_str2, "r") as jj_r:
                    puntos_imortalidad = int(jj_r.read())

                    with open(jugador_str2, "w") as jj_w:
                        jj_w.write(puntos_imortalidad)
    except IOError:





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
