import numpy as np
from turbopy import Simulation, PhysicsModule

class Projectile(PhysicsModule):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        self.position == np.zeros((1,2))
        self.velocity == np.zeros((1,2))
        self.f_drag == np.zeros((1,2))
        self.mass == input_data.get('mass', 1)
        self.push = owner.find_tool_by_name(input_data["pusher"]).push
    
    def initialize(self):
        self.position[:] = np.array(self._input_data["x0"])
        self.velocity[:] = np.array(self._input_data["v0"])
    
    def exchange_resources(self):
        self.publish_resource({"Position": self.position})
        self.publish_resource({"Velocity": self.velocity})
        self.publish_resource({"F_drag": self.f_drag})
        self.publish_resource({"Mass": self.mass})
    
    def update(self):
        self.push(self.position, self.velocity, self.f_drag, self.mass)
