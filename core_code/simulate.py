import numpy as np
import turbopy

configuration = {
        "Grid": {},
        "Clock": {},
        "PhysicsModules": {},
        "Tools": {}
        "Diagnostics": {}
        }

sim = turbopy.Simulation(configuration)
sim.run()
