"""Tests for the PhysicsModule projectile"""
from turbopy import PhysicsModule, Simulation
import numpy as np
import pytest
from pyatmos import coesa76
from astro_physics import Projectile

sample_input = {"Clock": {"start_time": 0, "end_time": 10, "dt": 10 ** -3},
                "Grid": {"N": 2, "x_min": 0, "x_max": 1},
                "PhysicsModules": {
                    "Projectile": {
                        "x0": [[0], [5000]],
                        "v0": [[0], [0]],
                        "mass": 100,
                        "c_d": 1,
                        "area": 15,
                        "pusher": "Leapfrog"
                    }
                },
                "Tools": {
                    "Leapfrog": {}
                    },
                "Diagnostics": {}}

def test_update_changes_parameters():
    owner = Simulation(sample_input)
    owner.prepare_simulation()

    test_projectile = Projectile(owner, sample_input)

    pos_init = test_projectile.position
    vel_init = test_projectile.velocity

    test_projectile.update()
    
    assert pos_init != test_projectile.position
    assert vel_init != test_projectile.velocity
