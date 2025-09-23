# Hardware Setup

## Drone Hardware

### Camera: A8 Gimbal Camera
- Stabilized 3-axis (yaw, pitch, roll)
- Outputs: Ethernet, CVBS, Micro-HDMI
- Input ports: S.Bus, UART, Ethernet UDP/TCP
- Voltage: 11-25.2V (3S-6S LiPo)

#### Control Options
- S.Bus: Traditional RC or SIYI ground station for main control.
- UART: SIYI Gimbal SDK, 115200 baud, 8N1.
- Ardupilot/Mavlink: SToRM32 gimbal protocol supported.

## Ground Station Hardware

### MK32 Features
- 7" HD touchscreen, 1000 nit
- Dual-channel HD video (15–30 km)
- Android OS, 8-core CPU, 4GB RAM, 64GB ROM
- Multiple channels, PWM support, SIM/TF slots
- IP4X waterproof, -10°C to 50°C operation

### Communication
- UART, USB (COM/CP2102), Bluetooth, UDP (default port 19856), WiFi/AP modes

## System Design Notes
- Light SLAM methods: ARCore/OpenVSLAM for Android; advanced SLAM via LAN/SIM streaming to server.
- Sensors: Barometer, LiDAR for extra spatial awareness and fail-safes.

[See reference: file:1]
