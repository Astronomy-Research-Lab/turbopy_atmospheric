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
    
    def push(self, position, velocity, net_force, mass):
        """Updates velocity and position vectors
        
        f{n+1} = function of x{n} and other stuff
        x{n+1} = x{n} + dt * v{n}
        v{n+1} = v{n} + dt * a{n+1}

        """
        "update net force here"
        position = position + self.dt * velocity
        velocity = velocity + self.dt * net_force / mass

ComputeTool.register("Leapfrog", Leapfrog)
