from __future__ import absolute_import, division, print_function

import math
import time

import numpy as np

import meshcat

vis = meshcat.Visualizer(zmq_url="tcp://localhost:6000").open()

capsule = meshcat.geometry.Capsule(0.1, 0.5)
vis["/meshcat/capsule"].set_object(capsule)
vis["/meshcat/capsule"].set_transform(meshcat.transformations.translation_matrix(np.array([0, 0, 1])))
box = meshcat.geometry.Box([0.5, 0.5, 0.5])
vis["/meshcat/box"].set_object(box)

draw_times = []

vis["/Background"].set_property("top_color", [1, 0, 0])

for i in range(2000):
    theta = (i + 1) / 100 * 2 * math.pi
    now = time.time()
    vis.set_transform(meshcat.transformations.rotation_matrix(theta, [0, 0, 1]))
    draw_times.append(time.time() - now)
    time.sleep(0.01)

print(sum(draw_times) / len(draw_times))
