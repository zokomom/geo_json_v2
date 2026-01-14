# geo_json_v2
Updated version of my previous geo_json.py that uses requests module instead of urllib. Also includes better error handling and Unicode support.

# Address Geocoding Tool (Python)

A Python command-line application that converts user-entered addresses into structured geographic information using the Geoapify Geocoding API. This project demonstrates API integration, JSON parsing, error handling, and Unicode support in Python.

## Features
- Converts an address into detailed location data
- Extracts country, state, city, postcode, latitude and longitude
- Displays formatted address and place ID
- Handles invalid input and API errors safely
- Supports multilingual (Unicode) place names
- Masks API key while printing request details

## Technologies Used
- Python 3
- requests
- urllib.parse
- json
- Geoapify Geocoding API

## Installation
1. Clone the repository
2. Install dependencies:  
   `pip install requests`
3. Run the script:  
   `python geoJSON.py`

## Usage
- Enter an address when prompted
- Provide a valid Geoapify API key
- View structured geographic information in the output

## API Key Note
Do not commit real API keys to GitHub.  
Enter the API key at runtime as prompted.

## Learning Outcomes
- Working with REST APIs
- Parsing JSON responses
- Handling HTTP status codes
- Unicode handling in Python
- Defensive programming practices

## License
This project is licensed under the MIT License.
