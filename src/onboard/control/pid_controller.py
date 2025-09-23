"""
Cascaded PID Controller for Drone Position & Attitude
"""
class PIDController:
    def __init__(self, kp, ki, kd, max_out=float('inf')):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral, self.prev_error = 0, 0
        self.max_out = max_out

    def update(self, setpoint, measurement, dt):
        error = setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        output = max(min(output, self.max_out), -self.max_out)
        self.prev_error = error
        return output
