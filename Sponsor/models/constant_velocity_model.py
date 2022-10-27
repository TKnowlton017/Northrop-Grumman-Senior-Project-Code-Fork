
import matplotlib.pyplot as plt
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

        fig = plt.figure()
        fig.show()
        plt.axis([0, 20, 0, 50000])

        prev_pos = self.initial_position + (self.unit_time * self.initial_velocity)
        prev_vel = self.initial_velocity

        for i in range(iterations):
            measurement = self.measured_values[i]
            # state update
            curr_pos = prev_pos + self.alpha*(measurement - prev_pos)
            curr_vel = prev_vel + self.beta*((measurement - prev_pos) / self.unit_time)
            # state extrapolation
            next_pos = curr_pos + (self.unit_time * curr_vel)
            next_vel = curr_vel
            #plot results
            print(f"iteration: {i}, position: {curr_pos}, velocity: {curr_vel}")
            plt.plot(i, curr_pos, 'k+')
            plt.plot(i, curr_vel, 'b*')
            plt.pause(0.05)
            plt.draw()
            # prepare for next iteration
            prev_pos = curr_pos
            prev_vel = curr_vel
            curr_pos = next_pos
            curr_vel = next_vel

model = ConstantVelocityModel(initial_position=30000, initial_velocity=40, unit_time=5, alpha=0.5, beta=0.5)
model.set_measurements([30110, 30265, 30740, 30750, 31135, 31015, 31180, 31610, 31960, 31865, 32200, 32400, 32600, 32800, 34000])
model.AB_filter(15)