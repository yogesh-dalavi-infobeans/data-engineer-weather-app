import requests
import mysql.connector
from datetime import datetime
import pytz

CITY = 'Pune'

DB_CONFIG = {
    'host': 'localhost',
    'user': 'yogesh',
    'password': 'root@123',
    'database': 'weather_db'
}

def fetch_weather():
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude=18.5196&longitude=73.8554&current=temperature_2m,relative_humidity_2m&start_date=2024-01-01&end_date=2025-05-25"
    )
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def process_data(data):
    temp = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    condition = ""  # This API does not provide conditions (like Clear, Rainy)
    return temp, humidity, condition

def insert_to_db(temp, humidity, condition):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    today = datetime.now(pytz.timezone('Asia/Kolkata')).date()
    cursor.execute("""
        INSERT INTO daily_weather (date, city, temperature_c, humidity, `condition`)
        VALUES (%s, %s, %s, %s, %s)
    """, (today, CITY, temp, humidity, condition))
    conn.commit()
    conn.close()

def run():
    data = fetch_weather()
    if data:
        temp, humidity, condition = process_data(data)
        insert_to_db(temp, humidity, condition)
        print("Data saved.")
    else:
        print("Failed to fetch weather.")

if __name__ == '__main__':
    run()
