from __future__ import absolute_import, division, print_function

import math
import time

import numpy as np

import meshcat

vis = meshcat.Visualizer(zmq_url="tcp://localhost:6000")

capsule = meshcat.geometry.Capsule(0.1, 0.5)
vis["/meshcat/capsule"].set_object(capsule)
vis["/meshcat/capsule"].set_transform(meshcat.transformations.translation_matrix(np.array([0, 0, 1])))

for i in range(500):
    time.sleep(0.01)
    vis["/meshcat/capsule"].set_property("opacity", i / 500)
    # vis["/meshcat/capsule"].set_property("color", [0, 1, 0, 0.1])
