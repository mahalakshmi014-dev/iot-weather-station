# IoT Weather Station

## Project Overview
A simulated IoT Weather Station using ESP32, DHT22 sensor, and ThingSpeak cloud dashboard. The system reads temperature and humidity data and sends it to ThingSpeak for real-time visualization.

## Components Used
- ESP32 Microcontroller
- DHT22 Temperature & Humidity Sensor
- ThingSpeak IoT Cloud Platform
- Wokwi Online Simulator
- Python (for data simulation)

## Circuit Connections
| DHT22 Pin | ESP32 Pin |
|-----------|-----------|
| VCC | 3.3V |
| GND | GND |
| SDA (DATA) | GPIO 15 |
| NC | Not Connected |

## Features
- Real-time temperature monitoring
- Real-time humidity monitoring
- Data visualization on ThingSpeak dashboard
- WiFi connectivity using ESP32
- Simulated using Wokwi online simulator and Python script

## How It Works
1. ESP32 reads temperature and humidity from DHT22 sensor every 20 seconds
2. Data is sent to ThingSpeak cloud via HTTP GET request
3. ThingSpeak displays live graphs for both temperature and humidity
4. A Python script (simulate.py) was used to test the ThingSpeak integration by sending simulated sensor readings

## ThingSpeak Dashboard
- Field 1: Temperature (°C)
- Field 2: Humidity (%)
- Channel ID: 3405702

## Files
- `weather_station.ino` - ESP32 firmware code (Arduino)
- `simulate.py` - Python script to simulate sensor data and test ThingSpeak API

## Output
See uploaded screenshots for CMD output and ThingSpeak graph results.

## Technologies Used
- Arduino C++ (ESP32 firmware)
- Python (data simulation)
- ThingSpeak API
- Wokwi Simulator
