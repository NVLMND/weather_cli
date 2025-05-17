# weather_cli ☁️

A Python-based terminal tool to fetch **current** and **forecast** weather data for any city using [WeatherAPI](https://www.weatherapi.com/).  
All queries are logged and stored locally in `weather_history.json`.

---

## Features

- Get **current weather**: temperature, humidity, wind, and condition
- Get **forecast**: max/min/avg temp, rain/snow chance, wind, condition
- Stores all lookups with timestamps in a local history file
- CLI-native: runs on Termux, Linux, macOS, Windows
- Works with any global city

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/NVLMND/weather_cli.git
cd weather-cli
