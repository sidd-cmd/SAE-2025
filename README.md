# SAE-2025
Autonomous drone system for SAE competition featuring object detection, disaster identification, and payload delivery.
# SAE Autonomous Drone Mission

Autonomous drone system for SAE competition featuring object detection, disaster identification, and payload delivery.

## Features
- YOLOv8-based object detection and classification
- PID-controlled drone alignment and stabilization
- Real-time communication with ground station
- Disaster situation identification (fire, flood, damage)
- Autonomous payload delivery from 10m altitude
- Emergency procedures and fail-safe mechanisms

## Hardware Requirements
- A8 Gimbal Camera with 3-axis stabilization
- MK32 Ground Station with Android OS
- IMU, GPS, LiDAR sensors
- NVIDIA Jetson or similar embedded system

## System Architecture 
# On Board Modules
<img width="876" height="533" alt="image" src="https://github.com/user-attachments/assets/be4e9498-e08c-4ebe-93c2-0c9669beeb87" />
# Ground Station
<img width="483" height="336" alt="image" src="https://github.com/user-attachments/assets/fc1414e5-4322-4850-a5b5-dfc884fbd9c8" />


## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Configure hardware in `src/shared/config/config.yaml`
3. Run simulations: `python simulations/airsim/drone_simulator.py`
4. Deploy to drone: `scripts/deployment/build_drone.sh`

# The code present in the given repo is largly starter code so make use of it at your own risk!!


