import json
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def generate_apology(customer, city, weather):
    return f"Hi {customer}, your order to {city} is delayed due to {weather.lower()}. We appreciate your patience!"

async def fetch_weather(session, order):
    city = order["city"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        async with session.get(url) as response:
            data = await response.json()
            
            if response.status != 200:
                error_data = await response.text()
                print(f"Error for city: {city} → {error_data}")
                return order

            weather_main = data["weather"][0]["main"]

            if weather_main in ["Rain", "Snow", "Extreme", "Clouds"]:
                order["status"] = "Delayed"
                print(generate_apology(order["customer"], city, weather_main))

            return order

    except Exception as e:
        print(f"Failed for {city}: {e}")
        return order

async def main():
    with open("orders.json", "r") as f:
        orders = json.load(f)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, order) for order in orders]
        updated_orders = await asyncio.gather(*tasks)

    with open("orders.json", "w") as f:
        json.dump(updated_orders, f, indent=2)

    print("✅ Done updating orders!")

asyncio.run(main())