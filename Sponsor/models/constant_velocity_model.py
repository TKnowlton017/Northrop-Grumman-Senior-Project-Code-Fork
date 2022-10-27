
import matplotlib.pyplot as plt
import numpy as np
import time

class ConstantVelocityModel:
    def __init__(self, initial_position, initial_velocity, unit_time, alpha, beta):
        self.initial_position = initial_position
        self.initial_velocity = initial_velocity
        self.unit_time = unit_time
        self.alpha = alpha
        self.beta = beta
        self.iteration = 0
        self.measured_values = []
        
    def set_measurements(self, values):
        self.measured_values = values

    def add_measurement(self, value):
        self.measured_values.append(value)

    def AB_filter(self, iterations):
        prev_pos = self.initial_position + (self.unit_time * self.initial_velocity)
        prev_vel = self.initial_velocity
        positions = []
        velocities = []
        for i in range(iterations):
            measurement = self.measured_values[i]
            # state update
            curr_pos = prev_pos + (self.alpha*(measurement - prev_pos))
            curr_vel = prev_vel + (self.beta*((measurement - prev_pos)/self.unit_time))
            # state extrapolation
            next_pos = curr_pos + (self.unit_time * curr_vel)
            next_vel = curr_vel
            #store results
            positions.append(curr_pos)
            velocities.append(curr_vel)
            # prepare for next iteration
            print(prev_pos, prev_vel)
            prev_pos = next_pos
            prev_vel = next_vel

        x = np.arange(0, 10, 1)
        fig, ax = plt.subplots()
        ax.plot(positions, color='red')
        ax.tick_params(axis='y', labelcolor='red')
        ax2 = ax.twinx()
        ax2.plot(velocities, color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        #ax.plot(x, velocities)
        plt.show()
        print(velocities)

model = ConstantVelocityModel(initial_position=30000, initial_velocity=40, unit_time=5, alpha=0.2, beta=0.1)
model.set_measurements([30110, 30265, 30740, 30750, 31135, 31015, 31180, 31610, 31960, 31865])
model.AB_filter(10)
