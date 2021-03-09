import numpy as np
from pyatmos import coesa76
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

        self.top = input_data.get("top")
        self.step = input_data.get("alt_step")
        self.altitude = np.zeros(int(self.maximum/self.step))
        self.density = self.altitude[:]
        self.temperature = self.altitude[:]
        self.pressure = self.altitude[:]
    
    def initialize(self):
        self.position[:] = np.array(self._input_data["x0"])
        self.velocity[:] = np.array(self._input_data["v0"])

        self.altitude[:] = list(range(int(self.maximum/self.step)))
        self.altitude[:] = [alt*self.step for alt in self.altitude]
        self.density[:], self.temperature[:], self.pressure[:] = coesa76(self.altitude)
        
        self.c_d = self._input_data["c_d"]
        self.p_h = self._input_data["p_h"]
    
    def exchange_resources(self):
        self.publish_resource({"Projectile:Position": self.position})
        self.publish_resource({"Projectile:Velocity": self.velocity})
        self.publish_resource({"Projectile:F_drag": self.f_drag})
        self.publish_resource({"Projectile:Mass": self.mass})
    
    def update(self):
        self.p_h = self.density.get(int((self.position[0, 1]/self.step)))
        self.push(self.position, self.velocity, self.mass, self.c_d, self.p_h, self.area)
