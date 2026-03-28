# Yellow.ai Assignment 2

This project is a Python script that processes order data and checks weather conditions using the OpenWeather API.

## Features
- Reads order data from a JSON file
- Fetches weather data for each city
- Updates order status based on weather conditions
- Handles invalid city errors

## Technologies Used
- Python
- OpenWeather API
- Async programming (for parallel API calls)

## How to Run
1. Install required libraries:
   pip install aiohttp python-dotenv

2. Add your API key in a .env file:
   API_KEY=your_api_key

3. Run the script:
   python main.py

## Output
- Updates order status in orders.json
- Prints delay messages and handles errors
