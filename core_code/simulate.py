import numpy as np
from turbopy import Simulation, ComputeTool, PhysicsModule, Diagnostic
from astro_tools import Leapfrog
from astro_physics import Projectile
from astro_diagnostics import ProjectileDiagnostic

configuration = {
    "Clock": {"start_time": 0,
              "end_time": 10,
              "dt": 0.1},
    "PhysicsModules": {
        "Projectile": {"mass": 1,
                       "c_d": 0.5,
                       "p_h": 0,
                       "area": 1,
                       "x0": [0, 6477999, 0],
                       "v0": [100, 0, 0],
                       "pusher": "Leapfrog"}},
    "Tools": {"Leapfrog": {}},
    "Diagnostics": {"directory": "output_atmos/",
                    "output_type": "csv",
                    "clock": {"filename": "time.csv"},
                    "ProjectileDiagnostic": [
                        {'component': 'position', 'filename': 'proj_x.csv'},
                        {'component': 'velocity', 'filename': 'proj_v.csv'}
                        ]
                    }
    }

PhysicsModule.register("Projectile", Projectile)
Diagnostic.register("ProjectileDiagnostic", ProjectileDiagnostic)
ComputeTool.register("Leapfrog", Leapfrog)

sim = Simulation(configuration)
sim.run()
