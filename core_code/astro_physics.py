import numpy as np
import math
from pyatmos import coesa76
from turbopy import Simulation, PhysicsModule

class Projectile(PhysicsModule):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)

        self.sound_constant = 20.04687
        self.position = np.zeros((1,3))
        self.velocity = np.zeros((1,3))

        self.mass = input_data.get('mass', 1)
        self.c_d = input_data.get('c_d', 1)
        self.p_h = self._input_data["p_h"]
        self.mach = None
        self.area = input_data.get('area', 1)
        self.push = owner.find_tool_by_name(input_data["pusher"]).push

        self.top = input_data.get("top", 100000)
        self.step = input_data.get("step", 1000)
        self.altitude = np.zeros(int(self.top/self.step))
        self.density = coesa76(self.altitude)[0]
        self.temperature = coesa76(self.altitude)[1]
        self.pressure = coesa76(self.altitude)[2]
    
    def initialize(self):
        self.position[:] = np.array(self._input_data["x0"])
        self.velocity[:] = np.array(self._input_data["v0"])
        self.altitude[:] = list(range(int(self.top/self.step)))
        self.altitude[:] = [alt * self.step / 1000 for alt in self.altitude]
        self.density[:], self.temperature[:], self.pressure[:] = coesa76(self.altitude)
        R = math.sqrt(self.position[0, 0] ** 2 + self.position[0, 1] ** 2)
        self.mach = self.sound_constant * math.sqrt(self.temperature[int(R - 6378000)//self.step])
    
    def exchange_resources(self):
        self.publish_resource({"Projectile:position": self.position})
        self.publish_resource({"Projectile:velocity": self.velocity})
        self.publish_resource({"Projectile:mass": self.mass})

    def update(self):
        R = math.sqrt(self.position[0, 0] ** 2 + self.position[0, 1] ** 2)
        V = math.sqrt((self.velocity[0, 0] ** 2) + (self.velocity[0, 1] ** 2))
        self.p_h = self.density[int(R - 6378000)//self.step]
        self.mach = self.sound_constant * math.sqrt(self.temperature[int(R - 6378000)//self.step])
        self.mach = V / self.mach
        self.push(self.position, self.velocity, self.mass, self.c_d, self.p_h, self.area)
