# Weather CLI App

A simple command-line weather tool built in Python.  
Fetches current weather data using the WeatherAPI service.  
Caches results locally in `cache.json` to reduce API calls and enable offline lookups.

## Features

- Get current weather for any city  
- Cache weather data  
- View cached city weather  
- List all cached cities  
- Delete individual cached cities  
- Clear entire cache  

## Requirements

- Python 3.x  
- `requests` library  
- WeatherAPI API key  

## Usage

```bash
# install dependencies
pip install requests

# run the script
python script_name.py
