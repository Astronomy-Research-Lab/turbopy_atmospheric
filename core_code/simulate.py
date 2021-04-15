import numpy as np
from turbopy import Simulation, ComputeTool, PhysicsModule, Diagnostic
from astro_tools import Leapfrog
from astro_physics import Projectile
from astro_diagnostics import ProjectileDiagnostic
import tkinter as tk

window = tk.Tk()
window.title("Initial conditions")
frm = tk.Frame(master = window)

lbl_vel = tk.Label(master = frm, text = "Entry velocity (km/s):")
ent_vel = tk.Entry(master = frm, width = 20)
lbl_ang = tk.Label(master = frm, text = "Entry angle (\N{DEGREE SIGN}):")
ent_ang = tk.Entry(master = frm, width = 20)
lbl_coef = tk.Label(master = frm, text = "Drag coefficient:")
ent_coef = tk.Entry(master = frm, width = 20)

frm.pack()
lbl_vel.grid(row = 0, column = 0, padx = 5, sticky = 'w')
ent_vel.grid(row = 0, column = 1, padx = 5)
lbl_ang.grid(row = 1, column = 0, padx = 5, sticky = 'w')
ent_ang.grid(row = 1, column = 1, padx = 5)
lbl_coef.grid(row = 2, column = 0, padx = 5, sticky = 'w')
ent_coef.grid(row = 2, column = 1, padx = 5)

window.mainloop()


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
