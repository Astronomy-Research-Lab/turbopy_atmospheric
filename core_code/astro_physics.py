import numpy as np
from turbopy import Simulation, PhysicsModule

class Projectile(PhysicsModule):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        self.position = np.zeros((1,3))
        self.velocity = np.zeros((1,3))
        self.mass = input_data.get('mass', 1)
        self.c_d = input_data.get('c_d', 1)
        self.p_h = None
        self.area = input_data.get('area', 1)
        self.push = owner.find_tool_by_name(input_data["pusher"]).push
    
    def initialize(self):
        self.position[:] = np.array(self._input_data["x0"])
        self.velocity[:] = np.array(self._input_data["v0"])
    
    def exchange_resources(self):
        self.publish_resource({"Projectile:position": self.position})
        self.publish_resource({"Projectile:velocity": self.velocity})
        self.publish_resource({"Projectile:mass": self.mass})
    
    def update(self):
        "update p_h here"
        self.push(self.position, self.velocity, self.mass, self.c_d, self.p_h, self.area)
