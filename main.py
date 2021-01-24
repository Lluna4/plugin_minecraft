import threading
import datetime
from mcapi import *
from org.bukkit.event.entity import PlayerDeathEvent
from org.bukkit.event.player import PlayerRespawnEvent
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player import PlayerVelocityEvent
from org.bukkit.event.player import PlayerJoinEvent

#beta-dev0.6
def conexion(e):
    jugador = e.getPlayer()
    jugador_str = str(jugador)
    jugador_str2 = jugador_str + "!"
    try:
        with open(jugador_str, "r") as j_r:
            dia = int(j_r.read())
            dia_ahora = datetime.datetime.now()
            if dia_ahora.day - dia > 0:
                with open(jugador_str, "w") as j_w:
                    j_w.write(str(dia_ahora.day))

                with open(jugador_str2, "r") as jj_r:
                    cosa = int(jj_r.read())
                    puntos_imortalidadX = dia_ahora.day - dia
                    puntos_imortalidad = cosa + puntos_imortalidadX


                    with open(jugador_str2, "w") as jj_w:
                        jj_w.write(str(puntos_imortalidad))
    except IOError:
        with open(jugador_str, "w") as jjjj_w:
            dia_ahora1 = datetime.datetime.now()           
            jjjj_w.write(str(dia_ahora1.day))
        with open(jugador_str2, "w") as jjjjjjj_w:
            jjjjjjj_w.write("0")
            





def dano_mortal(e):
    global vida_infinita
    entidad = e.getEntity()
    entidad_str = str(entidad)
    vida_infinita = False
    if entidad_str[:11] == "CraftPlayer":
        vida = float(entidad.getHealth())
        vida_str = str(vida)
       
        if e.getDamage() >= vida:
            nombre1 = entidad_str[17:-1]
            nombre = "CraftPlayer{name=%s}!" %nombre1
            try:
                with open(nombre, "r") as t_r:
                    inmortalidad = t_r.read()
                    inmortalidad_int = int(inmortalidad)
            except IOError:
                inmortalidad = 0
            
            if inmortalidad_int > 0:
                yell("REVIVE!!!!!!!!!!!!!!!!")
                entidad.setHealth(20.0)
                lugar = entidad.getLocation()
                entidad.spawnParticle(Particle.SOUL, lugar, 100)
                entidad.playSound(lugar, Sound.ENTITY_LIGHTNING_BOLT_THUNDER, 1.5, 1)
                inmortalidad_int -= 1
                inmortalidad = str(inmortalidad_int)
                with open(nombre, "w") as ttttt_w:
                    ttttt_w.write(inmortalidad)
                #vida_infinita = True
                #t = threading.Timer(60, se_acabo)
                #t.start()
        
   

        
        

        



listener = add_event_listener(EntityDamageEvent, dano_mortal)
listener2 = add_event_listener(PlayerJoinEvent, conexion)
