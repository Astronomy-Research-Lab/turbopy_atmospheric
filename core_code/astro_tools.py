import numpy as np
import math
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
    
    def push(self, position, velocity, mass, c_d, p_h, area):
        """Updates velocity and position vectors
        
        f_drag = (-1/2) * c_d * p_h * V^2 * S * (v{n}/V)
        f_grav = -G * M_e * r{n}/ R^3
        f{n+1} = f_drag + f_grav
        r{n+1} = r{n} + dt * r{n}
        v{n+1} = v{n} + dt * f{n+1}/m

        """
        
        G = 6.674 * 10 ** -11
        M_e = 5.972 * 10 ** 24
        R = math.sqrt(position[0, 0] ** 2 + position[0, 1] ** 2)
        V = math.sqrt(velocity[0, 0] ** 2 + velocity[0, 1] ** 2)
        f_drag = (-1/2) * c_d * p_h * V * area * velocity
        f_grav = -1 * G * M_e * position / (R ** 3)
        f_net = f_drag + f_grav
        if R <= 6378000:
            velocity = np.array([0, 0, 0])
            position = np.array([6378000*position[0, 0]/R,
                                 6378000*position[0, 1]/R,
                                 0])
            f_net = 0
        position[:] = position + self.dt * velocity
        velocity[:] = velocity + self.dt * f_net / mass