# File: p (Python 2.4)

from pirates.teleport.AreaTeleportActor import AreaTeleportActor

class PlayerAreaTeleportActor(AreaTeleportActor):
    
    def __init__(self, cr, name = 'PlayerAreaTeleportActor'):
        AreaTeleportActor.__init__(self, cr, name)


