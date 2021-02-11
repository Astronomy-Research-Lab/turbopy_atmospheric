"Tests for the compute_tools within the simulation"

import numpy as np
import pytest
from turbopy import Simulation, ComputeTool
from TurboPy-Atmospheric.astro_tools import Leapfrog
from pyatmos import coesa76

def test_init_should_create_object():
    "Creates a Leapfrog object to test that Leapfrog.__init__() creates an object"
    initial = Leapfrog(Simulation({"type": "Leapfrog"}), {"type": "Leapfrog"})
    assert isinstance(initial, Leapfrog)


def test_straight_fall():
    "Tests the funcionality for a 1-kg object falling from 1 km starting from rest\
    Assumes no atmosphere"

    input_data = {"Clock": {"start_time": 0, "end_time": 200, "dt": 10 ** -2},
                  "type": "Leapfrog",
                  "Grid": {"N":1, "min": 0, "max": 1},
                  "PhysicsModules": {}}
    owner = Simulation(input_data)
    owner.prepare_simulation()
    leap_tester = Leapfrog(owner, input_data)
    mass = 1
    pos_init = np.zeros((2,1))
    pos_init[:] = [[0], [1000]]
    vel_init = np.zeros((2,1))
    vel_init[:] = [[0],[0]]
    clock = input_data["Clock"]

    for x in range(100):
        leap_tester.push(pos_init, vel_init, mass, 0, 0, 1)

    pos_final = [0, 995.0918]
    vel_final = [0, -9.8165]

    assert np.allclose(pos_init, pos_final, rtol = .001, atol = .01)
    assert np.allclose(vel_init, vel_final, rtol = .001, atol = .01)

