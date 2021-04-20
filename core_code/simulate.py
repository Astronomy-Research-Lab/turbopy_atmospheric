import numpy as np
from turbopy import Simulation, ComputeTool, PhysicsModule, Diagnostic
from astro_tools import Leapfrog
from astro_physics import Projectile
from astro_diagnostics import ProjectileDiagnostic
import tkinter as tk
import math

def run():
    """Reference values: mass = 1000, c_d = 0.5, area = 1, vel = 0, ang = 0"""
    mass = float(ent_mass.get())
    c_d = float(ent_coef.get())
    area = float(ent_area.get())
    vel = float(ent_vel.get())
    rad = float(ent_ang.get()) * math.pi / 180
    
    v0 = [vel * math.cos(rad), -1 * vel * math.sin(rad), 0]
    
    configuration = {
    "Clock": {"start_time": 0,
              "end_time": 10,
              "dt": 0.1},
    "PhysicsModules": {
        "Projectile": {"mass": mass,
                       "c_d": c_d,
                       "p_h": 0,
                       "area": area,
                       "x0": [0, 6477999, 0],
                       "v0": v0,
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
    
    window.destroy()

window = tk.Tk()
window.title("Initial conditions")
frm = tk.Frame(master = window)

lbl_vel = tk.Label(master = frm, text = "Entry velocity (m/s):")
ent_vel = tk.Entry(master = frm, width = 20)
lbl_ang = tk.Label(master = frm, text = "Entry angle (\N{DEGREE SIGN}):")
ent_ang = tk.Entry(master = frm, width = 20)
lbl_coef = tk.Label(master = frm, text = "Drag coefficient:")
ent_coef = tk.Entry(master = frm, width = 20)
lbl_area = tk.Label(master = frm, text = "Front area (m^2):")
ent_area = tk.Entry(master = frm, width = 20)
lbl_mass = tk.Label(master = frm, text = "Mass (kg):")
ent_mass = tk.Entry(master = frm, width = 20)
btn_run = tk.Button(master = window, text = "Run", command = run)

frm.pack()
lbl_vel.grid(row = 0, column = 0, padx = 5, sticky = 'w')
ent_vel.grid(row = 0, column = 1, padx = 5)
lbl_ang.grid(row = 1, column = 0, padx = 5, sticky = 'w')
ent_ang.grid(row = 1, column = 1, padx = 5)
lbl_coef.grid(row = 2, column = 0, padx = 5, sticky = 'w')
ent_coef.grid(row = 2, column = 1, padx = 5)
lbl_area.grid(row = 3, column = 0, padx = 5, sticky = 'w')
ent_area.grid(row = 3, column = 1, padx = 5)
lbl_mass.grid(row = 4, column = 0, padx = 5, sticky = 'w')
ent_mass.grid(row = 4, column = 1, padx = 5)
btn_run.pack()

window.mainloop()
