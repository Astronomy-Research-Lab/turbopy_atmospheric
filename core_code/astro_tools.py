import numpy as np
from turbopy import Simulation, ComputeTool

class Leapfrog(ComputeTool):
    """Uses Leapfrog integration Method to increment values
    
    [Put equations here, must be able to increment position
     and velocity based on acceleration]"""
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        self.dt = None
    
    def initialize(self):
        self.dt = self._owner.clock.dt
    
    def push(self, position, velocity, f_drag, mass):
        """Updates velocity and position vectors
        
        f{n+1} = function of x{n} and other stuff
        x{n+1} = x{n} + dt * v{n}
        v{n+1} = v{n} + dt * a{n+1}

        """
        f_net = f_drag + "f_grav (make correct later when other stuff is written"
        position = position + self.dt * velocity
        velocity = velocity + self.dt * f_net / mass

ComputeTool.register("Leapfrog", Leapfrog)
