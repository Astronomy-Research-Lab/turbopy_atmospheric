import numpy as np
from turbopy import Simulation, PhysicsModule

class Projectile(PhysicsModule):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        pass
    
    def initialize(self):
        pass
    
    def exchange_resources(self):
        pass
    
    def update(self):
        pass