from django.shortcuts import render
from sqlalchemy import create_engine
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

DB_CONFIG = {
    'host': 'localhost',
    'user': 'yogesh',
    'password': 'root@123',
    'database': 'weather_db'
}
def fetch_data(filter_option):
    engine = create_engine("mysql+mysqlconnector://yogesh:root%40123@localhost/weather_db")
    if filter_option == '7days':
        start_date = (datetime.now() - timedelta(days=7)).date()
        query = f"SELECT date, temperature_c, humidity FROM daily_weather WHERE date >= '{start_date}' ORDER BY date"
    elif filter_option == '30days':
        start_date = (datetime.now() - timedelta(days=30)).date()
        query = f"SELECT date, temperature_c, humidity FROM daily_weather WHERE date >= '{start_date}' ORDER BY date"
    else:
        query = "SELECT date, temperature_c, humidity FROM daily_weather ORDER BY date"

    df = pd.read_sql(query, engine)
    return df

def generate_chart(df):
    plt.figure(figsize=(10, 4))
    plt.plot(df['date'], df['temperature_c'], marker='o', label='Temp (°C)', color='orange')
    plt.plot(df['date'], df['humidity'], marker='x', label='Humidity (%)', color='blue')
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.title("Weather Trends")
    plt.legend()
    plt.tight_layout()
    plt.savefig("weatherApp/static/chart.png")
    plt.close()

def index(request):
    filter_option = request.GET.get('filter', 'all')  # default to all
    df = fetch_data(filter_option)
    if not df.empty:
        generate_chart(df)
    table_html = df.to_html(classes='data', index=False)
    return render(request, 'index.html', {'table': table_html, 'chart': 'chart.png', 'selected_filter': filter_option})