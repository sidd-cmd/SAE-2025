# System Architecture

## Onboard Drone Modules
- **Perception**: Camera, IMU, GPS, LiDAR data processing
- **Control**: PID controllers for stabilization and alignment
- **Communication**: Data transmission to ground station

## Ground Station Modules
- **Detection**: YOLO processing and object classification
- **Planning**: Mission planning and command generation
- **UI**: Real-time monitoring and data display

## Communication Protocol
- Uplink: Video + sensor data with timestamping
- Downlink: Control commands with encryption
- Fallback: Onboard emergency procedures
