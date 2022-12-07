from matrix import *

def kalman_filter(x, P):
    for n in range(len(measurements)):
        # measurement update
        y = matrix([[measurements[n]]]) - H * x
        s = H * P * H.transpose() + R
        K = P * H.transpose() * s.inverse()
        x = x + K * y
        P = (I - K * H) * P
             
        # prediction
        x = F * x + u
        P = F * P * F.transpose()
    return x,P

measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x, P))