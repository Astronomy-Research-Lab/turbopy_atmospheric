import numpy as np
import turbopy

configuration = {
        "Clock": {"start_time": 0,
                  "end_time": 10,
                  "dt": 0.1},
        "PhysicsModules": {"mass": 1,
                           "c_d": 0.5,
                           "area": 1,
                           "x0": [0, 3881000],
                           "pusher": "Leapfrog"},
        "Tools": {"Leapfrog": {}},
        "Diagnostics": {}
        }

sim = turbopy.Simulation(configuration)
sim.run()
