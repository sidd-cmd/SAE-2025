"""
Drone Stabilization using PID Loops
"""
from .pid_controller import PIDController

class DroneStabilizer:
    def __init__(self):
        self.pid_pitch = PIDController(1.2, 0.0, 0.05, max_out=15)
        self.pid_roll = PIDController(1.2, 0.0, 0.05, max_out=15)
        self.pid_yaw = PIDController(1.0, 0.0, 0.03, max_out=10)
    
    def stabilize(self, setpoints, imu_data, dt):
        # setpoints: dict {'pitch': X, 'roll': Y, 'yaw': Z}
        control = {
            'pitch': self.pid_pitch.update(setpoints['pitch'], imu_data['pitch'], dt),
            'roll': self.pid_roll.update(setpoints['roll'], imu_data['roll'], dt),
            'yaw': self.pid_yaw.update(setpoints['yaw'], imu_data['yaw'], dt)
        }
        return control
