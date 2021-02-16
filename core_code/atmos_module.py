import numpy as np
from pyatmos import coesa76
from turbopy import Simulation, PhysicsModule

class AtmosModule(PhysicsModule):
    def __init__(self, owner: Simulation, input_data: dict):
        super.__init__(owner, input_data)
        self.maximum = input_data.get("max_alt")
        self.step = input_data.get("alt_step")
        self.altitude = np.zeros(int(self.maximum/self.step))
        self.density = np.zeros(self.altitude.len())
        self.temperature = np.zeros(self.altitude.len())
        self.pressure = np.zeros(self.altitude.len())

    def initialize(self):
        h = 0
        temp = []
        while h <= self.maximum:
            temp.append(h)
            h += self.step
        self.altitude[:] = np.array(temp)
        self.density[:], self.temperature[:], self.pressure[:] = coesa76(temp)
        
    def exchange_resources(self):
        self.publish_resource({"Atmosphere:Altitude": self.altitude})
        self.publish_resource({"Atmosphere:Density": self.density})
        self.publish_resource({"Atmosphere:Pressure": self.pressure})
        self.publish_resource({"Atmosphere:Temperature": self.temperature})

    def update(self):
        pass            #I don't think we need to run update, but it needs to be instantiated
